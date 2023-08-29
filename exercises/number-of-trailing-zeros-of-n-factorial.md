<div class="markdown prose max-w-none mb-8" id="description"><p>Write a program that will calculate the number of trailing zeros in a factorial of a given number.</p>
<p><code>N! = 1 * 2 * 3 *  ... * N</code></p>
<p>Be careful <code>1000!</code> has 2568 digits...</p>
<p>For more info, see: <a href="http://mathworld.wolfram.com/Factorial.html" data-turbolinks="false" target="_blank">http://mathworld.wolfram.com/Factorial.html</a> </p>
<h2 id="examples">Examples</h2>
<pre><code class="language-python"><span class="cm-variable">zeros</span>(<span class="cm-number">6</span>) <span class="cm-operator">=</span> <span class="cm-number">1</span>
<span class="cm-comment"># 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --&gt; 1 trailing zero</span>

<span class="cm-variable">zeros</span>(<span class="cm-number">12</span>) <span class="cm-operator">=</span> <span class="cm-number">2</span>
<span class="cm-comment"># 12! = 479001600 --&gt; 2 trailing zeros</span>
</code></pre>
<p><em>Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.</em></p>
</div>
