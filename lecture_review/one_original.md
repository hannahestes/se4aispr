# Review1

### **Topic 1: Data Representation & Pre-processing**

**1. Normalization (Min-Max)**

* **(a) [Understand]** Why is it algorithmically necessary to normalize data (scale 0..1) before calculating the distance between two rows?
* **(b) [Apply]** A dataset has a column "LinesOfCode" . A new module has 300 lines. Calculate its normalized score ().
1a. It is necessary because you don't want one attribute to be unecessarily weighted if it is not more important. By normalizing all values to 0..1, it levels the playing field of all attribute values.
1b. max - min / max


**2. Handling Symbolic Data**

* **(a) [Recall]** In the class's CSV standard, how does the algorithm distinguish between a column of numbers and a column of symbols (e.g., "Gender")?
* **(b) [Analyze]** If you tried to calculate the "mean" of a symbolic column like `[Apple, Banana, Apple]`, it fails. What specific statistical transformation is used instead to represent the central tendency of symbols?

2a. capital vs lowercase letter?
2b. Rather than mean, we would want to use mode and entropy, rather than mean and standard deviation.

**3. The "Heaven" Point**

* **(a) [Recall]** Define the "Heaven" point in the context of multi-objective optimization (e.g., for a car with `MPG` and `Horsepower`).
* **(b) [Apply]** If we want to *minimize* weight (normalized 0..1) and *maximize* safety (normalized 0..1), what are the coordinate values of the "Heaven" point?

3a. Heaven is the "perfect" or ideal number. Typically for an attribute like MGP, heaven would be a ridiculous;y high number.
3b. Weight would be 0 and MGP would be 1 for heaven.

**4. Euclidean Distance**

* **(a) [Understand]** What does the Euclidean distance formula measure between a data row and the "Heaven" point?
* **(b) [Create]** Write the pseudocode or mathematical notation for calculating the distance  between a row  with  columns and the Heaven point .

4a. The distance between two points.
4b. sqrt(a^2+b^2) where a and b are the coordinates

**5. Data Headers & Goals**

* **(a) [Recall]** In the course CSV format, what does a `+` or `-` at the end of a column name indicate (e.g., `weight-`, `acceleration+`)?
* **(b) [Evaluate]** If a column has no `+` or `-` (e.g., `Age`), how should the optimization algorithm treat it compared to those that do?

5a. It tells you whether you want to maximize or minimize that value; in other words it tells you what heaven is once it is normalized.
5b. Categorical data/disregard? Or use it to calculate the mode.

---

### **Topic 2: Statistical Heuristics**

**6. Cohen’s Rule (Effect Size)**

* **(a) [Recall]** State the definition of a "small effect" according to Cohen’s rule in this class (formula involving Standard Deviation).
* **(b) [Apply]** Algorithm A has a mean score of 80. Algorithm B has a mean of 82. The Standard Deviation of the population is 10. Is the difference between A and B a "small effect" or a meaningful change? Show calculation.

6a. Small effect is the case where given the mean (or average) of a set of values if an additional outlier was added, it would not largely effect the mean.
6b. Cohen = 90th percentile - 10th percentile / 2.56

90th percentile = Mean + (1.28 * std) = 92.8, 94.8
10th percentile = Mean + (-1.28 * std) = 67.2, 69.2

Cohen = 92.8 - 67.2 / 2.56 = 10
      = 94.8 - 69.2 / 2.56 = 10

So small effect?

**7. Standard Deviation (Variance)**

* **(a) [Understand]** What property of a dataset does Standard Deviation quantify?
* **(b) [Analyze]** In an optimization search, if the standard deviation of the current population drops to near zero, what does this indicate about the diversity of your solutions?

7a. variance?
7b. there is none

**8. Expected Values (Mode vs. Mean)**

* **(a) [Recall]** What is the "Expected Value" for a column of symbols?
* **(b) [Apply]** Given the list `[A, B, A, C, A, B]`, calculate the probability of the Expected Value.

8a. Mode
8b. A: .5, B: .33, C: .17

**9. The "Half of You Die" Heuristic**

* **(a) [Understand]** Explain the recursive strategy described in class where "half the data is discarded" at each step.
* **(b) [Analyze]** Why is this logarithmic reduction () considered a "massive shortcut" compared to typical Deep Learning approaches?

9a. It removes half of the data because it is more likely it not be useful.
9b. Because it takes a lot less resources.

**10. Sampling Validity**

* **(a) [Recall]** The lecturer claims we don't need to look at all data. What justification is given for using small samples (e.g., in the SQLite example)?
* **(b) [Evaluate]** If you only sample 100 points from a space of 3 billion, what assumption are you making about the "shape" of the solution space?

10a. We can get "close enough" without wasting a ton of resources.
10b. Relatively balanced?

---

### **Topic 3: Optimization Algorithms**

**11. Genetic Algorithms: The Metaphor**

* **(a) [Recall]** In the "Mommy, Daddy, Kid" metaphor, what does the "Kid" represent in terms of data structures?
* **(b) [Apply]** If Parent A is `[1, 1, 1]` and Parent B is `[0, 0, 0]`, create a "Kid" using a single-point crossover at index 1.

11a. The output of the genetic algorithm?
11b. .5?

**12. Mutation**

* **(a) [Understand]** What is the purpose of "mutation" in an evolutionary algorithm?
* **(b) [Analyze]** If you set the mutation rate to 0%, what risk does the algorithm face regarding "Local Optima"?

12a. It allows the algorithm to adapt to make ti better over time.
12b. Lots

**13. Simulated Annealing**

* **(a) [Recall]** How does Simulated Annealing decide whether to accept a "worse" solution during the search?
* **(b) [Apply]** In the "breakfast" metaphor, if you only ever eat the "best" cereal you currently know, what are you missing out on? How does "temperature" solve this?

13a. To try and escape a local maxima.
13b. This could be a local maxima and in reality there is a better cereal out there. Temperature helps by only allowing you to "like" it for so long.

**14. Stochasticity**

* **(a) [Understand]** Why might running the same optimization code twice produce different results?
* **(b) [Evaluate]** If a manager complains that your code "isn't deterministic," how do you use the concept of Cohen's Effect Size to prove the two different results are effectively the same?

14a. randomness
14b. if they give the same relative output then they are relatively deterministic "enough"

**15. Local vs. Global Optima**

* **(a) [Recall]** Define a "Local Optimum."
* **(b) [Analyze]** Why do greedy algorithms (that always take the best immediate step) often fail to find the Global Optimum?

15a. Given a dataset, there is a cluster and the local optimum is the best in that cluster.
15b. They get stuck on a local optimum.

---

### **Topic 4: Software Analytics & Research Concepts**

**16. Configuration Optimization (FLASH)**

* **(a) [Recall]** In the context of the SQLite case study, what was the goal of the optimization?
* **(b) [Apply]** If a system has 10 binary options (on/off), the search space is . If it has 50, it is . Explain why "brute force" testing is mathematically impossible for the second case.

16a. there are so many differnt configurations there is no way someone could test them all, so this is a way to minimize some of thsoe choices
16b. just way to many options and too many resources to use for brute force

**17. Transfer Learning**

* **(a) [Recall]** What is "Transfer Learning" in the context of software performance models (e.g., Valov et al.)?
* **(b) [Analyze]** If you train a model on "Data from 2020," why might it fail when tested on "Data from 2026"? What is this phenomenon called (often related to "Drift")?

17a. ...
17b. This idea of concept drift, but idk.

**18. "Garbage In, Garbage Out" (Labeling)**

* **(a) [Understand]** How does the quality of labels (e.g., "Bug" vs "Not Bug") affect the "ceiling" of model performance?
* **(b) [Evaluate]** If it costs $50 to verify a label manually, and you have 10,000 instances, propose a strategy to build a model without spending $500,000.

18a. hmmm
18b. randomly select $50 worth of instances

**19. Multi-Objective Trade-offs**

* **(a) [Recall]** What does it mean when two goals are "conflicting" (e.g., Speed vs. Memory)?
* **(b) [Analyze]** If you find a solution that improves Speed by 50% but increases Memory usage by 200%, is this a "better" solution? How does the "Distance to Heaven" metric help decide?

19a. If you want to maximize or minimize one, that directly conficts the other. One goes up and the other goes down, or other way around.
19b. Is there an option that imporves speed by 47% and only increases memory by 100%? The distance to heaven looks at all of the options and tries to find the near best given a few factors.

**20. The "Less is More" Principle**

* **(a) [Recall]** What is the core technical argument of "Less is More" regarding model complexity?
* **(b) [Evaluate]** You have a Linear Regression model (Accuracy 90%) and a Deep Transformer model (Accuracy 91%). Using the course philosophy, which do you choose and why?

20a. sometimes overcomplicating uses more resources, so by doing less we can optimize other options.
20b. linear regresson because it is only 1% less accurate but a lot simpler
