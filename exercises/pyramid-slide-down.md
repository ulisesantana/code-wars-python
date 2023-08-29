<div class="markdown prose max-w-none mb-8" id="description"><h3 id="lyrics">Lyrics...</h3>
<p>Pyramids are amazing! Both in architectural and mathematical sense. If you have a computer, you can mess with pyramids even if you are not in Egypt at the time. For example, let's consider the following problem. Imagine that you have a pyramid built of numbers, like this one here:</p>
<pre><code>   /3/
  \7\ 4 
 2 \4\ 6 
8 5 \9\ 3
</code></pre>
<h3 id="here-comes-the-task">Here comes the task...</h3>
<p>Let's say that the <em>'slide down'</em> is the maximum sum of consecutive numbers from the top to the bottom of the pyramid. As you can see, the longest <em>'slide down'</em> is <code>3 + 7 + 4 + 9 = 23</code></p>
<p>Your task is to write a function that takes a pyramid representation as an argument and returns its <strong>largest</strong> <em>'slide down'</em>. For example:</p>
<pre><code>* With the input `[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]`
* Your function should return `23`.
</code></pre>
<h3 id="by-the-way">By the way...</h3>
<p>My tests include some extraordinarily high pyramids so as you can guess, brute-force method is a bad idea unless you have a few centuries to waste. You must come up with something more clever than that.</p>
<p>(c) This task is a lyrical version of <strong>Problem 18</strong> and/or <strong>Problem 67</strong> on <a href="https://projecteuler.net" data-turbolinks="false" target="_blank">ProjectEuler</a>.</p>
</div>
