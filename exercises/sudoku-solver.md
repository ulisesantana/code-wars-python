<div class="markdown prose max-w-5xl mx-auto overflow-x-auto break-words" id="description"><p>Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value <code>0</code> representing an unknown square. </p>
<p>The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.</p>
<p>For Sudoku rules, see <a href="http://en.wikipedia.org/wiki/Sudoku" data-turbolinks="false" target="_blank">the Wikipedia article</a>.</p>
<pre><code class="language-python"><span class="cm-variable">puzzle</span> <span class="cm-operator">=</span> [[<span class="cm-number">5</span>,<span class="cm-number">3</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">7</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>],
          [<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">5</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>],
          [<span class="cm-number">0</span>,<span class="cm-number">9</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>],
          [<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">3</span>],
          [<span class="cm-number">4</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">3</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">1</span>],
          [<span class="cm-number">7</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">2</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>],
          [<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">2</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>],
          [<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">4</span>,<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">5</span>],
          [<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">7</span>,<span class="cm-number">9</span>]]

<span class="cm-variable">sudoku</span>(<span class="cm-variable">puzzle</span>)
<span class="cm-comment"># Should return</span>
[[<span class="cm-number">5</span>,<span class="cm-number">3</span>,<span class="cm-number">4</span>,<span class="cm-number">6</span>,<span class="cm-number">7</span>,<span class="cm-number">8</span>,<span class="cm-number">9</span>,<span class="cm-number">1</span>,<span class="cm-number">2</span>],
[<span class="cm-number">6</span>,<span class="cm-number">7</span>,<span class="cm-number">2</span>,<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">5</span>,<span class="cm-number">3</span>,<span class="cm-number">4</span>,<span class="cm-number">8</span>],
[<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">8</span>,<span class="cm-number">3</span>,<span class="cm-number">4</span>,<span class="cm-number">2</span>,<span class="cm-number">5</span>,<span class="cm-number">6</span>,<span class="cm-number">7</span>],
[<span class="cm-number">8</span>,<span class="cm-number">5</span>,<span class="cm-number">9</span>,<span class="cm-number">7</span>,<span class="cm-number">6</span>,<span class="cm-number">1</span>,<span class="cm-number">4</span>,<span class="cm-number">2</span>,<span class="cm-number">3</span>],
[<span class="cm-number">4</span>,<span class="cm-number">2</span>,<span class="cm-number">6</span>,<span class="cm-number">8</span>,<span class="cm-number">5</span>,<span class="cm-number">3</span>,<span class="cm-number">7</span>,<span class="cm-number">9</span>,<span class="cm-number">1</span>],
[<span class="cm-number">7</span>,<span class="cm-number">1</span>,<span class="cm-number">3</span>,<span class="cm-number">9</span>,<span class="cm-number">2</span>,<span class="cm-number">4</span>,<span class="cm-number">8</span>,<span class="cm-number">5</span>,<span class="cm-number">6</span>],
[<span class="cm-number">9</span>,<span class="cm-number">6</span>,<span class="cm-number">1</span>,<span class="cm-number">5</span>,<span class="cm-number">3</span>,<span class="cm-number">7</span>,<span class="cm-number">2</span>,<span class="cm-number">8</span>,<span class="cm-number">4</span>],
[<span class="cm-number">2</span>,<span class="cm-number">8</span>,<span class="cm-number">7</span>,<span class="cm-number">4</span>,<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">6</span>,<span class="cm-number">3</span>,<span class="cm-number">5</span>],
[<span class="cm-number">3</span>,<span class="cm-number">4</span>,<span class="cm-number">5</span>,<span class="cm-number">2</span>,<span class="cm-number">8</span>,<span class="cm-number">6</span>,<span class="cm-number">1</span>,<span class="cm-number">7</span>,<span class="cm-number">9</span>]]
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-keyword">var</span> <span class="cm-def">puzzle</span> <span class="cm-operator">=</span> [
            [<span class="cm-number">5</span>,<span class="cm-number">3</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">7</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>],
            [<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">5</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>],
            [<span class="cm-number">0</span>,<span class="cm-number">9</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>],
            [<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">3</span>],
            [<span class="cm-number">4</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">3</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">1</span>],
            [<span class="cm-number">7</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">2</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>],
            [<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">2</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>],
            [<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">4</span>,<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">5</span>],
            [<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">7</span>,<span class="cm-number">9</span>]];

<span class="cm-variable">sudoku</span>(<span class="cm-variable">puzzle</span>);
<span class="cm-comment">/* Should return</span>
<span class="cm-comment">[[5,3,4,6,7,8,9,1,2],</span>
<span class="cm-comment">[6,7,2,1,9,5,3,4,8],</span>
<span class="cm-comment">[1,9,8,3,4,2,5,6,7],</span>
<span class="cm-comment">[8,5,9,7,6,1,4,2,3],</span>
<span class="cm-comment">[4,2,6,8,5,3,7,9,1],</span>
<span class="cm-comment">[7,1,3,9,2,4,8,5,6],</span>
<span class="cm-comment">[9,6,1,5,3,7,2,8,4],</span>
<span class="cm-comment">[2,8,7,4,1,9,6,3,5],</span>
<span class="cm-comment">[3,4,5,2,8,6,1,7,9]] </span>
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-variable">sudoku</span>([
  [<span class="cm-number">5</span>,<span class="cm-number">3</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">7</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>],
  [<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">5</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>],
  [<span class="cm-number">0</span>,<span class="cm-number">9</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>],
  [<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">3</span>],
  [<span class="cm-number">4</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">3</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">1</span>],
  [<span class="cm-number">7</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">2</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>],
  [<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">2</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>],
  [<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">4</span>,<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">5</span>],
  [<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">7</span>,<span class="cm-number">9</span>]
]); <span class="cm-comment">/* =&gt; [</span>
  <span class="cm-comment">[5,3,4,6,7,8,9,1,2],</span>
  <span class="cm-comment">[6,7,2,1,9,5,3,4,8],</span>
  <span class="cm-comment">[1,9,8,3,4,2,5,6,7],</span>
  <span class="cm-comment">[8,5,9,7,6,1,4,2,3],</span>
  <span class="cm-comment">[4,2,6,8,5,3,7,9,1],</span>
  <span class="cm-comment">[7,1,3,9,2,4,8,5,6],</span>
  <span class="cm-comment">[9,6,1,5,3,7,2,8,4],</span>
  <span class="cm-comment">[2,8,7,4,1,9,6,3,5],</span>
  <span class="cm-comment">[3,4,5,2,8,6,1,7,9]</span>
<span class="cm-comment">] */</span>
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">puzzle</span> <span class="cm-keyword">=</span> [[<span class="cm-number">5</span>,<span class="cm-number">3</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">7</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>],
          [<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">5</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>],
          [<span class="cm-number">0</span>,<span class="cm-number">9</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>],
          [<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">3</span>],
          [<span class="cm-number">4</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">3</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">1</span>],
          [<span class="cm-number">7</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">2</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>],
          [<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">2</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>],
          [<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">4</span>,<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">5</span>],
          [<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">7</span>,<span class="cm-number">9</span>]]

<span class="cm-variable">sudoku</span> <span class="cm-variable">puzzle</span>
<span class="cm-comment">{- Should return</span>
<span class="cm-comment">[[5,3,4,6,7,8,9,1,2],</span>
<span class="cm-comment"> [6,7,2,1,9,5,3,4,8],</span>
<span class="cm-comment"> [1,9,8,3,4,2,5,6,7],</span>
<span class="cm-comment"> [8,5,9,7,6,1,4,2,3],</span>
<span class="cm-comment"> [4,2,6,8,5,3,7,9,1],</span>
<span class="cm-comment"> [7,1,3,9,2,4,8,5,6],</span>
<span class="cm-comment"> [9,6,1,5,3,7,2,8,4],</span>
<span class="cm-comment"> [2,8,7,4,1,9,6,3,5],</span>
<span class="cm-comment"> [3,4,5,2,8,6,1,7,9]]</span>
<span class="cm-comment">-}</span>
</code></pre>
<pre style="display: none;"><code class="language-rust"><span class="cm-comment">// puzzle before</span>
<span class="cm-variable">puzzle</span> <span class="cm-operator">=</span> [
    [<span class="cm-number">5</span>,<span class="cm-number">3</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">7</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>],
    [<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">5</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>],
    [<span class="cm-number">0</span>,<span class="cm-number">9</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>],
    [<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">3</span>],
    [<span class="cm-number">4</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">3</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">1</span>],
    [<span class="cm-number">7</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">2</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">6</span>],
    [<span class="cm-number">0</span>,<span class="cm-number">6</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">2</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>],
    [<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">4</span>,<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">5</span>],
    [<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">8</span>,<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-number">7</span>,<span class="cm-number">9</span>]
  ]

<span class="cm-variable">sudoku</span>(&amp;<span class="cm-variable">mut</span> <span class="cm-variable">puzzle</span>);
<span class="cm-comment">// puzzle after</span>
 <span class="cm-variable">puzzle</span> <span class="cm-operator">==</span> [
    [<span class="cm-number">5</span>,<span class="cm-number">3</span>,<span class="cm-number">4</span>,<span class="cm-number">6</span>,<span class="cm-number">7</span>,<span class="cm-number">8</span>,<span class="cm-number">9</span>,<span class="cm-number">1</span>,<span class="cm-number">2</span>],
    [<span class="cm-number">6</span>,<span class="cm-number">7</span>,<span class="cm-number">2</span>,<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">5</span>,<span class="cm-number">3</span>,<span class="cm-number">4</span>,<span class="cm-number">8</span>],
    [<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">8</span>,<span class="cm-number">3</span>,<span class="cm-number">4</span>,<span class="cm-number">2</span>,<span class="cm-number">5</span>,<span class="cm-number">6</span>,<span class="cm-number">7</span>],
    [<span class="cm-number">8</span>,<span class="cm-number">5</span>,<span class="cm-number">9</span>,<span class="cm-number">7</span>,<span class="cm-number">6</span>,<span class="cm-number">1</span>,<span class="cm-number">4</span>,<span class="cm-number">2</span>,<span class="cm-number">3</span>],
    [<span class="cm-number">4</span>,<span class="cm-number">2</span>,<span class="cm-number">6</span>,<span class="cm-number">8</span>,<span class="cm-number">5</span>,<span class="cm-number">3</span>,<span class="cm-number">7</span>,<span class="cm-number">9</span>,<span class="cm-number">1</span>],
    [<span class="cm-number">7</span>,<span class="cm-number">1</span>,<span class="cm-number">3</span>,<span class="cm-number">9</span>,<span class="cm-number">2</span>,<span class="cm-number">4</span>,<span class="cm-number">8</span>,<span class="cm-number">5</span>,<span class="cm-number">6</span>],
    [<span class="cm-number">9</span>,<span class="cm-number">6</span>,<span class="cm-number">1</span>,<span class="cm-number">5</span>,<span class="cm-number">3</span>,<span class="cm-number">7</span>,<span class="cm-number">2</span>,<span class="cm-number">8</span>,<span class="cm-number">4</span>],
    [<span class="cm-number">2</span>,<span class="cm-number">8</span>,<span class="cm-number">7</span>,<span class="cm-number">4</span>,<span class="cm-number">1</span>,<span class="cm-number">9</span>,<span class="cm-number">6</span>,<span class="cm-number">3</span>,<span class="cm-number">5</span>],
    [<span class="cm-number">3</span>,<span class="cm-number">4</span>,<span class="cm-number">5</span>,<span class="cm-number">2</span>,<span class="cm-number">8</span>,<span class="cm-number">6</span>,<span class="cm-number">1</span>,<span class="cm-number">7</span>,<span class="cm-number">9</span>]
  ]
</code></pre>
</div>
