![portada_notion_anki](https://github.com/user-attachments/assets/e5ce274b-9e7e-43c2-9b94-591a2c106c03)

Imagen de una nota de Notion convertida en una tarjeta de Anki:
![2025-03-01_15:21:15](https://github.com/user-attachments/assets/7c6760f8-d72f-4796-86a8-3086f8b1fbe2)

Código HTML de una nota de Notion convertida en tarjeta de Anki:
```html
<p>Son todos los números que <strong>pueden</strong> expresarse como el cociente efectuado o no efectuado de dos números enteros, ejemplos: $\frac{1}{2}, \frac{-\frac{7}{11}}{3\frac{5}{9}},\ -\frac{63}{352}$. <br>
    En el caso de $\frac{-\frac{1}{5}<br>
    }{\frac{1}{3}}$, aunque a primera vista ni el numerador ni el denominador son números enteros, podemos simplificarla para ver que en realidad puede expresarse como un cociente de dos enteros siendo obvio entonces que es un número racional:<br>
    $$<br>
    \frac{-\frac{1}{5}<br>
    }{\frac{1}{3}}<br>
    $$<br>
    Lo mismo que con $\frac{-\frac{1}{5}<br>
    }{\frac{1}{3}}$ pasa con cualquier otro número fraccionario, ejemplos: $\frac{1}{2}, \frac{-\frac{7}{11}}{3\frac{5}{9}},\ -\frac{63}{352}$.<br>
    Cuando decimos “cociente efectuado” nos referimos a por ejemplo $0,5$.<br>
    Cuando decimos “cociente no efectuado” nos referimos a por ejemplo $\frac{1}{2}$.<br>
    Cada número racional <strong>se define</strong> como una clase de equivalencia.<br>
    A la fracción irreducible se le conoce como ”representante canónico”.</p>
```

Imagen de una nota de Notion convertida en una tarjeta de Anki después de usar este complemento:
![2025-03-01_16:06:02](https://github.com/user-attachments/assets/87bfac18-22e4-4e3c-b2fa-43671d56db4f)


Código HTML de una nota de Notion convertida en tarjeta de Anki después de usar este complemento:
```html
<p>Son todos los números que <strong>pueden</strong> expresarse como el cociente efectuado o no efectuado de dos números enteros, ejemplos: [$]\frac{1}{2}, \frac{-\frac{7}{11}}{3\frac{5}{9}},\ -\frac{63}{352}[/$]. <br>
    En el caso de [$]\frac{-\frac{1}{5}<br>    }{\frac{1}{3}}[/$], aunque a primera vista ni el numerador ni el denominador son números enteros, podemos simplificarla para ver que en realidad puede expresarse como un cociente de dos enteros siendo obvio entonces que es un número racional:<br>
    [latex]\begin{math}
    \frac{-\frac{1}{5}
    }{\frac{1}{3}}
    \end{math}[/latex]<br>
    Lo mismo que con [$]\frac{-\frac{1}{5}<br>    }{\frac{1}{3}}[/$] pasa con cualquier otro número fraccionario, ejemplos: [$]\frac{1}{2}, \frac{-\frac{7}{11}}{3\frac{5}{9}},\ -\frac{63}{352}[/$].<br>
    Cuando decimos “cociente efectuado” nos referimos a por ejemplo [$]0,5[/$].<br>
    Cuando decimos “cociente no efectuado” nos referimos a por ejemplo [$]\frac{1}{2}[/$].<br>
    Cada número racional <strong>se define</strong> como una clase de equivalencia.<br>
    A la fracción irreducible se le conoce como ”representante canónico”.</p>
```

Debido a que Anki no logra renderizar la nota de Notion ya que no es la forma en que Anki usa LaTeX (HTML) he creado este complemento que reemplaza automáticamente caracteres de notas de Notion que han sido exportadas y convertidas en un archivo `.apkg`. 

¡De esta forma tus notas de Notion estarán listas para ser estudiadas!.

¡Es el verdadero "plug and play"!.

[![Ver demo](https://img.youtube.com/vi/)](https://youtu.be/OhBfxBoz76M)

### A tener en cuenta
Por alguna razón existen notas de Notion que al ser exportadas y convertidas en `.apkg` no tienen el código completo de LaTeX, ejemplos:

```html
<p>Establece que: Si $a,b \in \mathbb{R}$; entonces al compararlos se puede presentar solo uno de los siguientes casos:<br>
    [latex]\begin{math}<br>
    a&gt;b \ a</p>
```

Debido a esto no se me ocurre una expresión regular que elimine la etiqueta `<br>` sin eliminar el resto de etiquetas `<br>` que si queremos en el código HTML de la tarjeta de Anki.
