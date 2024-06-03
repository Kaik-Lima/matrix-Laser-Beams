# Matrix-Laser-Beams
 Exercício dinâmico intermediário LeetCode com Matrix, Array e Simulation. Com intenção em aprofundar conhecimentos em matrizes de forma interativa para uma eficiente manipulação em um conjunto de dados.

Anti-theft security devices are activated inside a bank. You are given a <strong>0-indexed</strong> binary string array <code>bank</code> representing the floor plan of the bank, which is an <code>m x n</code> 2D matrix. <code>bank[i]</code> represents the <code>i<sup>th</sup></code> row, consisting of <code>'0's</code> and <code>'1'</code>s. <code>'0'</code> means the cell is empty, while <code>'1'</code> means the cell has a security device.

There is <strong>one</strong> laser beam between any <strong>two</strong> security devices <strong>if both</strong> conditions are met:

<ul>
 <li>The two devices are located on two different rows: <code>r1</code> and <code>r2</code>, where <code>r1 < r2</code>.</li>
 <li>For each row <code>i</code> where <code>r1 < i < r2</code>, there are <strong>no security devices</strong> in the <code>i<sup>th</sup></code> row.</li>
</ul>
<br>Laser beams are independent, i.e., one beam does not interfere nor join with another.<br>
Return <em>the total number of laser beams in the bank.</em>

<h4>Example 1:</h4>
<img src='https://assets.leetcode.com/uploads/2021/12/24/laser1.jpg' style="width: 400px; height: 368px;">

<pre>
 <strong>Input:</strong> bank = ["011001","000000","010100","001000"]
 <strong>Output:</strong> 8
 <strong>Explanation:</strong> Between each of the following device pairs, there is one beam. In total, there are 8 beams:
  * bank[0][1] -- bank[2][1]
  * bank[0][1] -- bank[2][3]
  * bank[0][2] -- bank[2][1]
  * bank[0][2] -- bank[2][3]
  * bank[0][5] -- bank[2][1]
  * bank[0][5] -- bank[2][3]
  * bank[2][1] -- bank[3][2]
  * bank[2][3] -- bank[3][2]
 Note that there is no beam between any device on the 0<sup>th</sup> row with any on the 3<sup>rd</sup> row.
 This is because the 2<sup>nd</sup> row contains security devices, which breaks the second condition.
</pre>

<h4>Example 2:</h4>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/laser2.jpg" style="width: 244px; height: 325px;">
<pre>
 <strong>Input:</strong> bank = ["000","111","000"]
 <strong>Output:</strong> 0
 <strong>Explanation:</strong> There does not exist two devices located on two different rows.
</pre>

<h4>Constraints:</h4>
<ul>
	<li><code>m == bank.length</code></li>
	<li><code>n == bank[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>bank[i][j]</code> is either <code>'0'</code> or <code>'1'</code>.</li>
</ul>
