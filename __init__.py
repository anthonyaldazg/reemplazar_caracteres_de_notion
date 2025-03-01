import re
from aqt import mw
from aqt.qt import QAction, QInputDialog, QMessageBox
from anki.hooks import addHook

def reemplazar_signos(text):
    # Eliminar todas las coincidencias para <br> seguido de }
    text = re.sub(r'<br>', r'}', text, flags=re.MULTILINE)
    # Eliminar todas las coincidencias para <br> entre [latex]\begin{math} y \end{math}[/latex]
    text = re.sub(r'\[latex\]\\begin{math}(.*?)\\end{math}\[/latex\]', lambda m: '[latex]\\begin{math}' + re.sub(r'<br>', '', m.group(1)) + '\\end{math}[/latex]', text, flags=re.DOTALL)
    # Eliminar todas las coincidencias para <br /> entre [latex]\begin{math} y \end{math}[/latex]
    text = re.sub(r'\[latex\]\\begin{math}(.*?)\\end{math}\[/latex\]', lambda m: '[latex]\\begin{math}' + re.sub(r'<br />', '', m.group(1)) + '\\end{math}[/latex]', text, flags=re.DOTALL)
    # Eliminar todas las coincidencias para <br> justo después de cualquier =
    text = re.sub(r'=(<br>)', lambda m: '', text)
    # Eliminar todas las coincidencias para <br> justo antes de cualquier = 
    text = re.sub(r'(<br>)=', lambda m: '', text)
    # Depuración
    #QMessageBox.information(mw, "Depuración", f"eliminar_br:\n{text}")

    # Reemplazar todas las ocurrencias de \gt por &gt;
    text = re.sub(r'\\gt', '&gt;', text)
    # Reemplazar de &amp;gt; por &gt;
    text =  re.sub(r'&amp;gt;', '&gt', text)
    # Reemplazar los ### de cada línea por <h3> y al final de la línea donde lo encontró poner </h3>
    text = re.sub(r'^### (.*)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    # Reemplazar los &amp;#xfa; de cada línea por ú
    text = re.sub(r'&amp;#xfa;', r'ú', text, flags=re.MULTILINE)
    # Reemplazar &#x24;&#x24; por $$
    text = text.replace('&#x24;&#x24;', '$$')
    # Reemplazar &#x24; por $
    text = text.replace('&#x24;', '$')
    text = text.replace('&amp;#x24;', '$')
    # Eliminar todos los saltos de linea entre $$ y $$
    text = re.sub(r'\$(.*?)\$', lambda m: '$' + m.group(1).replace('\n', '') + '$', text, flags=re.DOTALL)
    # Primero, reemplazar todas las ocurrencias de $$ por [latex]\begin{math} y \end{math}[/latex]
    def reemplazar_dobles(text):
        matches_doble = list(re.finditer(r'(?<!\\)(?<!\$)(?<!\[latex\\begin\{math\})\$\$(?!\$)(?!\[latex\\end\{math\}\[/latex\])', text))
        counter = 1
        offset = 0
        for match in matches_doble:
            start, end = match.start() + offset, match.end() + offset
            if counter % 2 != 0:
                replacement = '[latex]\\begin{math}'
            else:
                replacement = '\\end{math}[/latex]'
            text = text[:start] + replacement + text[end:]
            offset += len(replacement) - (end - start)
            counter += 1
        return text

    # Luego, reemplazar todas las ocurrencias de $ por [$] y [/$], pero solo si no han sido reemplazadas previamente
    def reemplazar_simples(text):
        matches_simple = list(re.finditer(r'(?<!\\)(?<!\[latex\\begin\{math\})\$(?!\$)(?!\[latex\\end\{math\}\[/latex\])', text))
        counter = 1
        offset = 0
        for match in matches_simple:
            start, end = match.start() + offset, match.end() + offset
            if counter % 2 != 0:
                replacement = '[$]'
            else:
                replacement = '[/$]'
            text = text[:start] + replacement + text[end:]
            offset += len(replacement) - (end - start)
            counter += 1
        return text

    # Verificar si existen [$] y [/$] en el texto
    if '[$]' in text or '[/$]' in text:
        return text, True
    else:
        text = reemplazar_dobles(text)
        text = reemplazar_simples(text)
        return text, False

def reemplazar_en_tarjetas(deck_name):
    note_ids = mw.col.find_notes(f'"deck:{deck_name}"')
    processed_notes = set()
    modified_count = 0
    found_existing_signs = False

    while note_ids:
        for note_id in note_ids:
            if note_id in processed_notes:
                continue
            try:
                note = mw.col.get_note(note_id)
                note_modified = False
                for field in note.keys():
                    original_text = note[field]
                    modified_text, found = reemplazar_signos(original_text)
                    if found:
                        found_existing_signs = True
                    if original_text != modified_text:
                        note[field] = modified_text
                        note.flush()
                        note_modified = True
                if note_modified:
                    modified_count += 1
                processed_notes.add(note_id)
            except Exception as e:
                with open("anki_modification_errors.log", "a") as log_file:
                    log_file.write(f"Error modificando la nota {note_id}, del campo '{field}': {str(e)}\n")
        note_ids = [nid for nid in mw.col.find_notes(f'"deck:{deck_name}"') if nid not in processed_notes]

    if found_existing_signs:
        QMessageBox.information(mw, "Depuración", "Se encontraron [$] y [/$] en el texto, no se reemplazaron los signos simples.")
    QMessageBox.information(mw, "Estado de las tarjetas", f"Se modificaron {modified_count} notas.")

def mostrar_en_anki():
    action = QAction("Reemplazar delimitadores de LaTeX de Notion", mw)
    def activado():
        decks = mw.col.decks.all_names_and_ids()
        deck_names = [deck.name for deck in decks]
        deck_name, ok = QInputDialog.getItem(mw, "Seleccionar maso", "Elige un mazo:", deck_names, 0, False)
        if ok and deck_name:
            reemplazar_en_tarjetas(deck_name)
    action.triggered.connect(activado)
    mw.form.menuTools.addAction(action)

addHook("profileLoaded", mostrar_en_anki)
