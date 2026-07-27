# Eigen Decomposition: A Detailed Guide

_(Note: The topic of eigen decomposition may appear a bit mathematical. However, it is essential to understand this before moving on to Singular Value Decomposition (SVD). Those not interested in SVD may skip this topic.)_

To effectively use eigenvalues and eigenvectors, one must understand the concept of Eigen Decomposition.

### 1. The Core Concept

Previously, we established that if A is a square matrix, v is a non-zero vector, and λ is a scalar, the following relationship holds:

$Av=λ\vec{v}$ In this equation, the matrix $A$ acts on the vector $\vec{v}$ . The result is simply a scaled version of $\vec{v}$. This implies that matrix A does not change the direction of $\vec{v}$ , it only changes its magnitude by a factor of $\lambda.$ Note $\lambda$ is a scalar

* If λ=1, the matrix leaves the vector unchanged.
* If λ>1, the matrix "stretches" the vector.
* If 0<λ<1, the matrix "compresses" the vector.
* If λ<0, the direction is reversed.

### 2. The Logic Behind Decomposition

Why do we break a matrix apart? The logic is similar to understanding how a machine works by taking it apart into its components.

Suppose a square matrix $A$ (size $n \times n$) has $n eigenvalues $λ\_1$​,$λ\_2$​,$…,λ\_n$​ and corresponding eigenvectors $\vec{v\_1}$. $\vec{v\_2}$, $...... \vec{v\_n}$

We can arrange the eigenvectors as columns into a matrix $Q$

$Q =\[\vec{v\_1}$. $\vec{v\_2}$, $...... \vec{v\_n}]$

We can arrange the eigenvalues into a diagonal matrix $\Lambda$) (Capital Lambda):

$$
\Lambda =
\begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n
\end{bmatrix}
$$

Using the definition $Av=λ\vec{v}$, we can write a combined matrix equation for all eigenvectors simultaneously:

$AQ = Q\Lambda$ If the matrix $Q$ is invertible (which is true if the eigenvectors are linearly independent), we can multiply both sides by $Q^{-1}$ from the right:

We get: $AQQ^{-1} = Q\Lambda Q^{-1}$

Since $QQ^{-1} =1$, then we have

We have $A = Q\Lambda Q^{-1}$ This is the Eigen Decomposition. It reveals that the matrix A is actually (Considering $Q\Lambda Q^{-1}$ from right to left) a rotation ($Q^{-1}$), followed by a scaling ($\Lambda$), followed by a rotation back ($Q$).

## Flowchart of Eigen decomposition

![Eigen Decomposition](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-eigen-decomposition-steps.png)

## Interpretation

Eigen Decomposition represents:

```
A = Rotation → Scaling → Rotation back
```

### 3. Step-by-Step Mathematical Example

Let us take a real example to understand the math. Let:

$$
A=\left[\begin{array}{ccc}
3 & 1 & -1 \\
1 & 3 & -1 \\
-1 & -1 & 5
\end{array}\right]
$$

**Step 1: Find the Eigenvalues**

We must solve the characteristic equation $det(A−λI)=0$. Where

$$
I=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]
$$

**So we get**

$$
I=\left[\begin{array}{ccc}
3- \lambda & 1 & -1 \\
1 & 3-\lambda & -1 \\
-1 & -1 & 5-\lambda
\end{array}\right] =0
$$

Solving this cubic equation yields the eigenvalues:

$λ1​=6, λ2​=2, λ3​=3$

**Step 2: Find the Eigenvectors**

For each eigenvalue, we solve $(A−λI)\vec{v}\_1=0$.

### For $\lambda\_1 ​= 6:$

$$
(A-6 I) \vec{v}=\left[\begin{array}{ccc}
-3 & 1 & -1 \\
1 & -3 & -1 \\
-1 & -1 & -1
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\
0
\end{array}\right]
$$

Solving this system gives the eigenvector

$$
\text { eigenvector } \vec{v}_1=\left[\begin{array}{c}
-1 \\
-1 \\
2
\end{array}\right] .\left(\text { Normalized: } \frac{1}{\sqrt{6}}[-1,-1,2]^T\right) .
$$

### For λ2​=2:

$$
(A-2 I) \vec{v}=\left[\begin{array}{ccc}
1 & 1 & -1 \\
1 & 1 & -1 \\
-1 & -1 & 3
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\
0
\end{array}\right]
$$

Solving this system gives the eigenvector

$$
\text { eigenvector } \vec{v}_2=\left[\begin{array}{c}
-1 \\
1 \\
0
\end{array}\right] .\left(\text { Normalized: } \frac{1}{\sqrt{2}}[-1,1,0]^T\right) .
$$

### For λ3​=3:

$$
(A-3 I) \vec{v}=\left[\begin{array}{ccc}
0 & 1 & -1 \\
1 & 0 & -1 \\
-1 & -1 & 2
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\
0
\end{array}\right]
$$

Solving this system gives the eigenvector

$$
\text { eigenvector } \vec{v}_3=\left[\begin{array}{c}
1 \\
1 \\
1
\end{array}\right] .\left(\text { Normalized: } \frac{1}{\sqrt{3}}[1,1,1]^T\right) .
$$

**Step 3: Construct Matrices $Q$ and $\Lambda$**

We form matrix Q with normalized eigenvectors as columns and Λ with eigenvalues on the diagonal.

$$
Q=\left[\begin{array}{ccc}
-\frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} \\
-\frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} \\
\frac{2}{\sqrt{6}} & 0 & \frac{1}{\sqrt{3}}
\end{array}\right], \quad \Lambda=\left[\begin{array}{lll}
6 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 3
\end{array}\right]
$$

**Step 4: Verify Decomposition**

We verify that $A=QΛQ^{−1}$. Since A is symmetric, $Q$ is orthogonal, meaning $Q^{−1}=Q^T$ (the transpose).

$A=QΛQ^T$

If you perform the matrix multiplication $QΛQ^T$, you will recover the original matrix $A$.

### 4. Elaborate Discussion

Why is this important?

* **Dimensionality Reduction:** In Principal Component Analysis (PCA), eigenvalues tell us which directions (eigenvectors) contain the most information (variance). We keep the vectors with large λ and discard those with small λ.
* **Matrix Powers:** Calculating $A^100$ is hard. But using decomposition: $A^{100}=(QΛQ^{−1})^{100}=QΛ^{100}Q^{−1}$. Since Λ is diagonal, $Λ^{100}$ is just raising the diagonal elements to the power of 100. This makes computation trivial.
* **Symmetric Matrices:** For symmetric matrices ($A=A^T$), the eigenvectors are always orthogonal (vi​⋅vj​=0). This makes decomposition stable and is the foundation for spectral clustering and graph partitioning.

## Example script

The following script does the following:-

```python
# Eigen Decomposition in NumPy (Clean Version)

import numpy as np

# Step 1: Define the matrix A

A = np.array([
    [3,  1, -1],
    [1,  3, -1],
    [-1, -1, 5]
])

print("--- Original Matrix A ---")
print(A)

# Step 2: Eigenvalues & Eigenvectors

# np.linalg.eig returns:
# - eigenvalues (1D array). Note: For symmetric matrices, these are real numbers.
# - eigenvectors (columns of matrix). Each column corresponds to the eigenvector associated 
#   with the eigenvalue at the same index.

eig_vals, eig_vecs = np.linalg.eig(A)  
# eig_vals: [4, 4, 3], eig_vecs: columns are eigenvectors corresponding to these eigenvalues.

# Sort eigenvalues (descending) for clarity
idx = np.argsort(eig_vals)[::-1]  # Get indices that would sort eigenvalues in descending order
eig_vals = eig_vals[idx]  # Sort eigenvalues
eig_vecs = eig_vecs[:, idx]  # Reorder eigenvectors to match sorted eigenvalues (columns are eigenvectors)

print("--- Eigenvalues ---")
print(np.round(eig_vals, 3))  # Output: [4, 4, 3] (rounded to 3 decimal places)
# Note: The eigenvalues are repeated (4 appears twice), which indicates that there is a repeated eigenvalue.
# In this case, the matrix has a repeated eigenvalue of 4, which means there are multiple linearly independent 
# eigenvectors associated with that eigenvalue.
# The presence of repeated eigenvalues can lead to a situation where the matrix is not diagonalizable, 
# but in this case, since the matrix is symmetric, it is still diagonalizable and we can find a complete set of eigenvectors.


print("\n--- Matrix Q (Eigenvectors as columns) ---")
print(np.round(eig_vecs, 3))  # Output: Each column is an eigenvector corresponding to the eigenvalues in the same order.
# Note: The eigenvectors are normalized (unit length) and are orthogonal to each other due to the symmetry of the matrix A.

# Step 3: Construct Lambda (Diagonal)

# np.diag places values on diagonal. 
# Since eig_vals is a 1D array of eigenvalues, np.diag(eig_vals) creates a diagonal matrix 
# where the diagonal elements are the eigenvalues from eig_vals, and all off-diagonal elements are zero. 
# This matrix Lambda will have the eigenvalues on its diagonal, which is essential for reconstructing 
# the original matrix A using the eigen decomposition formula A = Q Λ Q⁻¹ (or A = Q Λ Qᵀ for symmetric matrices).

Lambda = np.diag(eig_vals)  # Lambda is a diagonal matrix with eigenvalues on the diagonal and zeros elsewhere.

print("--- Matrix Lambda (Diagonal Eigenvalues) ---")
print(np.round(Lambda, 3))  # [[4, 0, 0], [0, 4, 0], [0, 0, 3]] (rounded to 3 decimal places)
# Note: The matrix Lambda is a diagonal matrix where the diagonal elements are the eigenvalues of A.
# The off-diagonal elements are zero, which is a key property of the diagonal matrix in eigen decomposition.
# The diagonal matrix Lambda is crucial for understanding how the original matrix A can be reconstructed
# using the eigenvectors and eigenvalues, and it also plays a central role in the matrix power trick,
# where we can compute A^n by raising the eigenvalues in Lambda to the power n and then reconstructing A 
# using the eigenvectors.
# The eigenvalues in Lambda are the same as those in eig_vals, but arranged in a diagonal matrix form, 
# which is necessary for the matrix multiplication in the reconstruction step.


# Step 4: Verify A = Q Λ Q^T (symmetric case)
# For symmetric matrices:
# Q⁻¹ = Qᵀ (orthogonal property). 
# This means that the inverse of Q is equal to its transpose, which simplifies the reconstruction of A 
# from its eigen decomposition.
# The formula A = Q Λ Q⁻¹ can be rewritten as A = Q Λ Qᵀ for symmetric matrices,
# which is what we will verify here.
# We will compute Q Λ Qᵀ and check if it reconstructs the original matrix A.
# Note: Due to floating-point precision, we may see very small numerical differences, 
# but the reconstructed matrix should be very close to the original matrix A.
# The matrix multiplication Q Λ Qᵀ involves:
# 1. Multiplying Q (matrix of eigenvectors) by Λ (diagonal matrix of eigenvalues), which scales each eigenvector 
# by its corresponding eigenvalue.
# 2. Then multiplying the result by Qᵀ (transpose of Q), which combines the scaled eigenvectors back into the 
# original space, reconstructing the original matrix A. 
# The resulting matrix A_reconstructed should be equal to the original matrix A, confirming that the 
# eigen decomposition is correct.    
# The eigen decomposition allows us to express the original matrix A in terms of its eigenvalues and eigenvectors,
# which is a powerful tool for understanding the properties of the matrix and for performing various operations, 
# such as computing matrix powers, exponentials, and solving systems of linear equations.    


Q = eig_vecs
Q_T = Q.T

A_reconstructed = Q @ Lambda @ Q_T

print("--- Reconstructed Matrix A ---")
print(np.round(A_reconstructed, 3))
print()

# ---------------------------------------
# Step 5: Verify Matrix Power Trick
# ---------------------------------------
# A^n = Q Λ^n Q⁻¹
# Here Q⁻¹ = Qᵀ (since A is symmetric)

power = 3

# Method 1: Direct computation
A_direct = np.linalg.matrix_power(A, power)

# Method 2: Using eigen decomposition
Lambda_power = np.linalg.matrix_power(Lambda, power)
A_decomp = Q @ Lambda_power @ Q_T

print("--- Matrix Power A^3 ---")

print("\nDirect method:")
print(np.round(A_direct, 3))

print("\nUsing decomposition (Q Λ^3 Q^T):")
print(np.round(A_decomp, 3))

# ---------------------------------------
# Note:
# Small numerical differences may occur
# due to floating-point precision
# ---------------------------------------

```

<details>

<summary>Explanation of the script (Click to expand)</summary>

## Introductory Note (Based on This Script)

In this script, we work with the matrix:

A = \[\[ 3 1 -1]\
\[ 1 3 -1]\
\[-1 -1 5]]

This is a **symmetric matrix** (i.e., $A=A^T$), which is important because:

* All eigenvalues are **real**
* Eigenvectors are **orthogonal**
* $Q^{−1}=Q^T$ (used later in the script)

***

### Step 1: What does the matrix represent?

The matrix $A$ represents a **linear transformation** in 3D space.

When we multiply a vector $\vec{v}$ by $A$:

$\vec{w}=A\vec{v}$

we get a **new transformed vector**.

***

### Step 2: What are eigenvalues and eigenvectors (in this example)?

We compute:

`eig_vals, eig_vecs = np.linalg.eig(A)`

This gives:

* **Eigenvalues:** `[4, 4, 3]` (after sorting)
* **Eigenvectors:** columns of matrix `Q`

***

#### What does this mean for "this" matrix?

* The transformation stretches space by:
  * factor **4** in two directions
  * factor **3** in one direction

Important observation (comment in script explained):

> Eigenvalue **4 is repeated**

This means:

* There are **multiple independent directions** (eigenvectors) where scaling = 4
* The matrix still works fine because it is **symmetric → guaranteed diagonalizable**

***

### Step 3: Why do we sort eigenvalues?

`idx = np.argsort(eig_vals)[::-1]`

This is **not mathematically required**

It is done only to:

* keep eigenvalues in a consistent order (e.g., largest first)
* match manual calculations

***

### Step 4: What is Matrix Q?

Q = eig\_vecs

Matrix QQQ contains eigenvectors as columns:

$Q=\[\vec{v}\_1  \vec{v}\_2 \vec{v}\_3]$

* Each column corresponds to one eigenvalue
* Eigenvectors are **normalized (unit length)**
* Because matrix is symmetric → they are **orthogonal**

***

### Step 5: What is Lambda?

`Lambda = np.diag(eig_vals)`

This creates:

```
Lambda =  
[[4 0 0]  
 [0 4 0]  
 [0 0 3]]
```

Meaning:

* No mixing between directions
* Only **scaling along eigenvector directions**

***

### Step 6: What does $A = Q Λ Q^T$ mean

The script explains this very well—here’s the clean interpretation:

$A=Q\Lambda Q^T$

This means:

#### Step-by-step meaning

1. $Q^T$: Convert vector into eigenvector coordinate system
2. $\Lambda$ : Scale each component (by 4, 4, 3)
3. $Q$: Convert back to original coordinates

***

### Key Insight

> The matrix transformation becomes “pure scaling” in the eigenvector basis.

***

### Step 7: Why reconstruction works

`A_reconstructed = Q @ Lambda @ Q_T`

This works because:

* Eigenvectors form a complete basis
* Eigenvalues store scaling information

> So we can rebuild the original matrix exactly

***

### Step 8: Matrix Power Trick

Instead of:

$A^3=A⋅A⋅A$

we use:

$A^{3} =QΛ^{3}Q^{T}$

***

#### Why this works

Because:

$A =QΛQ^{−1}$

So:

$A^{n}=QΛnQ−1$

***

### What happens inside Lambda

$\Lambda^3 =$ \[\[4³ 0 0 ]\
\[0 4³ 0 ]\
\[0 0 3³]]

Only the diagonal values are raised to power (Since rest are all 0)

***

### How efficiency is obtained

* Direct multiplication → expensive
* Eigen decomposition → much faster

This is used in:

* machine learning
* differential equations
* simulations

***

## Floating-Point Comment (clarified)

`np.round(...)`

Needed because:

* computers store numbers approximately
*   tiny errors like:

    `1.0000000000000002`
* rounding makes output readable

</details>
