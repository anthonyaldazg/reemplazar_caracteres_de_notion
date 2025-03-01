Imagen de una nota de Notion convertida en una tarjeta de Anki:


Código HTML de una nota de Notion convertida en tarjeta de Anki:
```html
<p>Establece que: Si $a,b \in \mathbb{R}$; entonces al compararlos se puede presentar solo uno de los siguientes casos:<br>
    [latex]\begin{math}<br>
    a&gt;b \ a</p>
```

Imagen de una nota de Notion convertida en una tarjeta de Anki después de usar este complemento:


Código HTML de una nota de Notion convertida en tarjeta de Anki después de usar este complemento:
```html

```

Debido a que Anki no logra renderizar la nota de Notion ya que no es la forma en que Anki usa LaTeX (HTML) he creado este complemento que reemplaza automáticamente caracteres de notas de Notion que han sido exportadas y convertidas en un archivo `.apkg`. 

¡De esta forma tus notas de Notion estarán listas para ser estudiadas!.

¡Es el verdadero "plug and play"!.


### A tener en cuenta
Por alguna razón existen notas de notion que al ser exportadas y convertidas en `.apkg` no tienen el código completo de LaTeX, ejemplos:

```html
<p>Establece que: Si $a,b \in \mathbb{R}$; entonces al compararlos se puede presentar solo uno de los siguientes casos:<br>
    [latex]\begin{math}<br>
    a&gt;b \ a</p>
```

Debido a esto no se me ocurre una expresión regular que elimine la etiqueta `<br>` sin eliminar el resto de etiquetas `<br>` que si queremos en el código HTML de la tarjeta de Anki.
