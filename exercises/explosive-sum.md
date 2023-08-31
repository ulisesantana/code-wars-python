<div class="markdown prose max-w-none mb-8" id="description"><h1 id="how-many-ways-can-you-make-the-sum-of-a-number">How many ways can you make the sum of a number?</h1>
<p>From wikipedia: <a href="https://en.wikipedia.org/wiki/Partition_(number_theory)" data-turbolinks="false" target="_blank">https://en.wikipedia.org/wiki/Partition_(number_theory)</a></p>
<blockquote>
<p>In number theory and combinatorics, a partition of a positive integer <em>n</em>, also called an <em>integer partition</em>, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:</p>
</blockquote>
<pre><code>4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
</code></pre>
<h2 id="examples">Examples</h2>
<h3 id="basic">Basic</h3>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">sum</span>(<span class="cm-number">1</span>) <span class="cm-comment">// 1</span>
<span class="cm-variable">sum</span>(<span class="cm-number">2</span>) <span class="cm-comment">// 2  -&gt; 1+1 , 2</span>
<span class="cm-variable">sum</span>(<span class="cm-number">3</span>) <span class="cm-comment">// 3 -&gt; 1+1+1, 1+2, 3</span>
<span class="cm-variable">sum</span>(<span class="cm-number">4</span>) <span class="cm-comment">// 5 -&gt; 1+1+1+1, 1+1+2, 1+3, 2+2, 4</span>
<span class="cm-variable">sum</span>(<span class="cm-number">5</span>) <span class="cm-comment">// 7 -&gt; 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3</span>

<span class="cm-variable">sum</span>(<span class="cm-number">10</span>) <span class="cm-comment">// 42</span>
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">explosiveSum</span>  <span class="cm-number">1</span>   <span class="cm-comment">-- 1</span>
<span class="cm-variable">explosiveSum</span> <span class="cm-number">2</span>   <span class="cm-comment">-- 2 -&gt; 1+1 , 2</span>
<span class="cm-variable">explosiveSum</span> <span class="cm-number">3</span>   <span class="cm-comment">-- 3 -&gt; 1+1+1, 1+2, 3</span>
<span class="cm-variable">explosiveSum</span> <span class="cm-number">4</span>   <span class="cm-comment">-- 5 -&gt; 1+1+1+1, 1+1+2, 1+3, 2+2, 4</span>
<span class="cm-variable">explosiveSum</span> <span class="cm-number">5</span>   <span class="cm-comment">-- 7 -&gt; 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3</span>

<span class="cm-variable">explosiveSum</span> <span class="cm-number">10</span>  <span class="cm-comment">-- 42</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">exp_sum</span>(<span class="cm-number">1</span>) <span class="cm-comment"># 1</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">2</span>) <span class="cm-comment"># 2  -&gt; 1+1 , 2</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">3</span>) <span class="cm-comment"># 3 -&gt; 1+1+1, 1+2, 3</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">4</span>) <span class="cm-comment"># 5 -&gt; 1+1+1+1, 1+1+2, 1+3, 2+2, 4</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">5</span>) <span class="cm-comment"># 7 -&gt; 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3</span>

<span class="cm-variable">exp_sum</span>(<span class="cm-number">10</span>) <span class="cm-comment"># 42</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">exp_sum</span>(<span class="cm-number">1</span>) <span class="cm-comment"># 1</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">2</span>) <span class="cm-comment"># 2  -&gt; 1+1 , 2</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">3</span>) <span class="cm-comment"># 3 -&gt; 1+1+1, 1+2, 3</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">4</span>) <span class="cm-comment"># 5 -&gt; 1+1+1+1, 1+1+2, 1+3, 2+2, 4</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">5</span>) <span class="cm-comment"># 7 -&gt; 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3</span>

<span class="cm-variable">exp_sum</span>(<span class="cm-number">10</span>) <span class="cm-comment"># 42</span>
</code></pre>
<pre style="display: none;"><code class="language-cpp"><span class="cm-variable">exp_sum</span>(<span class="cm-number">1</span>) <span class="cm-comment">// 1</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">2</span>) <span class="cm-comment">// 2  -&gt; 1+1 , 2</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">3</span>) <span class="cm-comment">// 3 -&gt; 1+1+1, 1+2, 3</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">4</span>) <span class="cm-comment">// 5 -&gt; 1+1+1+1, 1+1+2, 1+3, 2+2, 4</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">5</span>) <span class="cm-comment">// 7 -&gt; 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3</span>

<span class="cm-variable">exp_sum</span>(<span class="cm-number">10</span>) <span class="cm-comment">// 42</span>
</code></pre>
<pre style="display: none;"><code class="language-go"><span class="cm-variable">ExpSum</span>(<span class="cm-number">1</span>) <span class="cm-comment">// 1</span>
<span class="cm-variable">ExpSum</span>(<span class="cm-number">2</span>) <span class="cm-comment">// 2 -&gt; 1+1 , 2</span>
<span class="cm-variable">ExpSum</span>(<span class="cm-number">3</span>) <span class="cm-comment">// 3 -&gt; 1+1+1, 1+2, 3</span>
<span class="cm-variable">ExpSum</span>(<span class="cm-number">4</span>) <span class="cm-comment">// 5 -&gt; 1+1+1+1, 1+1+2, 1+3, 2+2, 4</span>
<span class="cm-variable">ExpSum</span>(<span class="cm-number">5</span>) <span class="cm-comment">// 7 -&gt; 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3</span>

<span class="cm-variable">ExpSum</span>(<span class="cm-number">10</span>) <span class="cm-comment">// 42</span>
</code></pre>
<pre style="display: none;"><code class="language-rust"><span class="cm-variable">exp_sum</span>(<span class="cm-number">1</span>) <span class="cm-comment">// 1</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">2</span>) <span class="cm-comment">// 2  -&gt; 1+1 , 2</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">3</span>) <span class="cm-comment">// 3 -&gt; 1+1+1, 1+2, 3</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">4</span>) <span class="cm-comment">// 5 -&gt; 1+1+1+1, 1+1+2, 1+3, 2+2, 4</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">5</span>) <span class="cm-comment">// 7 -&gt; 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3</span>

<span class="cm-variable">exp_sum</span>(<span class="cm-number">10</span>) <span class="cm-comment">// 42</span>
</code></pre>
<h3 id="explosive">Explosive</h3>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">sum</span>(<span class="cm-number">50</span>) <span class="cm-comment">// 204226</span>
<span class="cm-variable">sum</span>(<span class="cm-number">80</span>) <span class="cm-comment">// 15796476</span>
<span class="cm-variable">sum</span>(<span class="cm-number">100</span>) <span class="cm-comment">// 190569292</span>
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">explosiveSum</span>  <span class="cm-number">50</span> <span class="cm-comment">--    204226</span>
<span class="cm-variable">explosiveSum</span>  <span class="cm-number">80</span> <span class="cm-comment">--  15796476</span>
<span class="cm-variable">explosiveSum</span> <span class="cm-number">100</span> <span class="cm-comment">-- 190569292</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">exp_sum</span>(<span class="cm-number">50</span>) <span class="cm-comment"># 204226</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">80</span>) <span class="cm-comment"># 15796476</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">100</span>) <span class="cm-comment"># 190569292</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">exp_sum</span>(<span class="cm-number">50</span>) <span class="cm-comment"># 204226</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">80</span>) <span class="cm-comment"># 15796476</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">100</span>) <span class="cm-comment"># 190569292</span>
</code></pre>
<pre style="display: none;"><code class="language-cpp"><span class="cm-variable">exp_sum</span>(<span class="cm-number">50</span>) <span class="cm-comment">// 204226</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">80</span>) <span class="cm-comment">// 15796476</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">100</span>) <span class="cm-comment">// 190569292</span>
</code></pre>
<pre style="display: none;"><code class="language-go"><span class="cm-variable">ExpSum</span>(<span class="cm-number">50</span>) <span class="cm-comment">// 204226</span>
<span class="cm-variable">ExpSum</span>(<span class="cm-number">80</span>) <span class="cm-comment">// 15796476</span>
<span class="cm-variable">ExpSum</span>(<span class="cm-number">100</span>) <span class="cm-comment">// 190569292</span>
</code></pre>
<pre style="display: none;"><code class="language-rust"><span class="cm-variable">exp_sum</span>(<span class="cm-number">50</span>) <span class="cm-comment">// 204226</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">80</span>) <span class="cm-comment">// 15796476</span>
<span class="cm-variable">exp_sum</span>(<span class="cm-number">100</span>) <span class="cm-comment">// 190569292</span>
</code></pre>
<p>See <a href="http://www.numericana.com/data/partition.htm" data-turbolinks="false" target="_blank">here</a> for more examples.</p>
</div>
