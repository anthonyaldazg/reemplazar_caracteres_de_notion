Ejemplo del código HTML de una nota de Nota de Notion convertida en tarjeta de Anki:
```html
<p>Establece que: Si $a,b \in \mathbb{R}$; entonces al compararlos se puede presentar solo uno de los siguientes casos:<br>
    [latex]\begin{math}<br>
    a&gt;b \ a</p>
```

### A tener en cuenta
Por alguna razón existen notas de notion que al ser exportadas y convertidas en `.apkg` no tienen el código completo de LaTeX, ejemplos:

```html
<p>Establece que: Si $a,b \in \mathbb{R}$; entonces al compararlos se puede presentar solo uno de los siguientes casos:<br>
    [latex]\begin{math}<br>
    a&gt;b \ a</p>
```

Debido a esto no se me ocurre una expresión regular que elimine la etiqueta `<br>` sin eliminar el resto de `<br>` que si queremos en el código HTML de la tarjeta de Anki.
