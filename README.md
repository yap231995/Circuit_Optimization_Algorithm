# Collection of Circuit Optimization Algorithm 
The codes here are reproduce of the algorithm for the linear components of the Circuit for my own understanding and hope to share whoever is trying to reproduce them also. <br>

##Paar Algorithm 
[1] We reproduce the code stated in https://ieeexplore.ieee.org.remotexs.ntu.edu.sg/document/613165 <br>
C. Paar, "Optimized arithmetic for Reed-Solomon encoders," Proceedings of IEEE International Symposium on Information Theory, 1997, pp. 250-, doi: 10.1109/ISIT.1997.613165.

[2] The idea in this algorithm follows a Greedy algorithm by picking two columns with the most Hamming weight. 
More information, read the paper stated in [1].

##BP Algorithm
TODO


##Low_Depth_Greedy
[1]This was stated in https://www.nist.gov/publications/depth-16-circuit-aes-s-box <br>
This algorithm was used to obtained one of the widely used depth 16 Sbox. <br>

[2] It consider the depth into account.
The algorithm uses phases to make sure the depths are under control. 
However, there are some error in the algorithm when considering the Hamming weight 2 first for more information read the following: 
https://www.nist.gov/publications/small-low-depth-circuits-cryptographic-applications.

##Rand_Greedy_Algorithm 
[1] This is found in https://www.nist.gov/publications/small-low-depth-circuits-cryptographic-applications.
The paper gives a lot of other concept such as See-Saw Methods.
Many improvement and consideration were also given. 
They give a new problem called Depth Constrain Linear Optimization (DCLO) problem

[2] The idea is to implement if the particular row whether is Feasible for the particular goal depth that was given.


