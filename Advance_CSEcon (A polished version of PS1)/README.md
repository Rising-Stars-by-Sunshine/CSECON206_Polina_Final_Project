# 📌 MILESTONE 2
## QUESTION 1
### Analyze your experience with oTree, identifying pain points in behavioral game theory research. Review related literature and class discussions to understand experimental economics' goals. Propose a software solution that outperforms oTree in at least three aspects, enhancing strategic interaction studies. Highlight why these advancements are crucial.

Albeit not having extensive experience working with oTree, having just discovered the platform through our class activities, I believe that oTree offers researchers a powerful and accessible platform for designing, conducting, and analyzing economic experiments and social science research studies. It has a relatively easy-to-understand pipeline and a sufficient body of guidelines on project development, for instance, the one provided by Professor Zhang in collaboration with DKU students back in 2021 (Zhang et al. 2021). It is undoubtedly a great tool for advancing our understanding of human behavior and decision-making in various contexts. However, like any software, it does have its limitations. I will refer to my example of attempting to design a Prisoner’s Dilemma game involving more stakeholders (since this experience can be useful for understanding more complex structures and algorithms at play), but the program only allowed me to work with two players and limited choice of the influence factors to some decisions (which, I want to point out, may have been due to my limited experience with the program, which I will need to breach in the future) (Figure 1). Therefore, I want to acknowledge that some potential areas for improvement of the interactive features of the platform may include scalability, internationalization and localization, and user interface customization. While oTree is great for small to medium-sized experiments, it can face challenges when scaling up to larger experiments with hundreds or thousands of participants. Enhancements could focus on optimizing performance and efficiency to handle larger experiments seamlessly. This might involve improvements in database management, caching mechanisms, or distributed computing. Additionally, oTree currently lacks comprehensive support for internationalization and localization, which can be a limitation for organizations like the World Bank that operate globally. Enhancements could involve adding support for multiple languages, currencies, and date formats, as well as addressing cultural differences in experiment design and presentation. Finally, while oTree provides a basic interface for experiment presentation, customization options are somewhat limited. Enhancements could involve providing more tools and flexibility for researchers to customize the look and feel of their experiments, including support for multimedia content, interactive elements, and responsive design for different devices. These three areas of advancement hold particular value to us and the researchers within the field because of more opportunities presented as a result of the implementation of these developments into the existing program. It is worth acknowledging that the software for oTree remains free and available for use, which can pose an obstacle for the developers to incorporate advanced changes into the existing software. However, having learned how many present companies on the technology market are interested in supporting the development of smaller companies/developers even with a limited financial gain during the conference with company representatives during Week 1 provides us hope that in the future the oTree software will see more developments integrated, or a different software developer will breach the gap.

![image](https://github.com/Rising-Stars-by-Sunshine/CSECON206_Polina/assets/148934457/aebaa8bc-b874-4a17-9bb9-61750d5ca11c)
Figure 1. oTree game experience. A personal screenshot of the student.

## QUESTION 2
### Delve into the limitations of current multi-agent reinforcement learning (MARL) frameworks, focusing on environment constraints and agent algorithm customizations. Choose a classic game (e.g., Prisoner's Dilemma, Battle of the Sexes, or the Trust Game) to illustrate these limitations. Describe the development process of a MARL agent for your selected game, detailing the definition of states, actions, and rewards grounded in fundamental behavioral assumptions. Your analysis should provide insights into overcoming MARL's current limitations, fostering advancements in the field.

Multi-agent reinforcement learning (MARL) is undoubtedly a tool of high utility when analyzing behavioral game theory largely due to its opportunity to grasp comprehensive dynamics between the group members and assess different social metrics. I had a personal experience witnessing one of the MARL algorithms unfold within the GoBigger game I played in my childhood - only under the name Agar.io (Zhang 2022) (Figure 2). The rules of the game are simple - the players consume particles and other players (smaller than yourself) to grow in size; the final goal of the game is to grow the biggest in size and occupy the whole playing area.

While this framework has seen significant advancements in the last couple of years, the framework still has some limitations. For analysis purposes, we will turn to the Prisonner’s Dilemma, previously discussed when referring to the first question, to allow us to look into potential development areas of this game in the MARL context. Some of the limitations of this dilemma within the scope of MARL include but are not limited to a constraining environment, which fails to account for larger dynamics, stemming outside of the direct outcomes of the decision (taking into account sentence longevity and financial payout). Then, MARL may not possess the capability at the moment to adapt to more complex problems or increased participant dimensions, which limits its potential at the current stage — but also gives ground for further improvements. In an attempt to address these limitations, we will need to account for the development process of a MARL agent within the Prisoner’s Dilemma. Initially, we must take into account the actions of the agent that are relevant to different situations/environments (cooperating or defecting), the previous actions of the opponent, and any other environmental variables that may be relevant. Next, we need to understand the options available to each person, which are either to cooperate or defect. Additionally, we need to consider the rewards or punishments that are given based on the outcomes. To improve the development process and execution, we can explore the development of more sophisticated environment models that would have the capability to capture the complex dynamics and social interactions pertaining to the nature of the game. Due to the complexity of implementing state-of-the-art technologies in collaboration with behavioral game theory, addressing the limitations with new algorithms may take some time.

![image](https://github.com/Rising-Stars-by-Sunshine/CSECON206_Polina/assets/148934457/ee9d1b21-3746-40e2-aef3-554e38736dd7)
Figure 2. GoBigger game experience. A personal screenshot of the student.

## QUESTION 3
### Critically engage with existing research in the field of federated learning, using the specific paper presented by the guest speaker as a primary example. Students will assess the paper's research questions, methodologies, and application scenarios and propose new research ideas addressing the identified limitations or gaps.

As we have comprehensively covered the paper during the brilliant discussion by Professor Bing Luo during Week 2, I decided to apply this skill to a different paper - (Figure 3).

## Paths to Equilibrium in Normal-Form Games by Bora Yongacoglu, Gürdal Arslan, Lacra Pavel, Serdar Yüksel

<img alt="Mindmap" src="https://github.com/Rising-Stars-by-Sunshine/CSECON206_Polina_Final_Project/assets/148934457/4ead7527-9311-4f54-a097-032fd55a9fa6">
Figure 3. Paths to Equilibrium in Normal-Form Games Mindmap. Chart created with gracious help from Markmap.

### Summary of the Paper
This paper delves into the intricacies of multi-agent reinforcement learning (MARL) scenarios, specifically examining sequences of strategies that adhere to pairwise constraints inspired by policy updating in reinforcement learning. It focuses on update functions satisfying a quasi-rationality condition called satisficing, which ensures stability in strategy profiles while allowing for exploratory updates. The central question addressed is whether it's always possible to construct a satisficing path from an initial strategy profile to a Nash equilibrium in a given normal-form game, with implications for the effectiveness of MARL algorithms.

### Core Research Questions
#### Feasibility of Satisficing Paths: 
Is it always possible to construct satisficing paths that terminate at equilibrium strategies in MARL scenarios?

#### Implications for MARL Algorithms: 
What are the implications of constructing satisficing paths for the capabilities or limitations of MARL algorithms?

### Methodologies
The paper employs theoretical analysis to explore the satisficing principle and its implications for MARL algorithms. It also involves formal mathematical proofs to establish the existence and properties of satisficing paths in normal-form games, potentially supplemented by computational simulations to validate theoretical findings.

### Application Scenarios
The research findings have implications for various applications, including:

- MARL algorithms: Enhancing the design and effectiveness of algorithms seeking Nash equilibrium.
- Multi-agent systems: Informing the behavior of autonomous agents in strategic interactions.
- Game theory: Advancing our understanding of equilibrium concepts and stability in strategic environments.

### Critique of the Research Question
While the research question addresses an important aspect of MARL dynamics, its narrow focus on satisficing paths in normal-form games may limit its applicability to broader MARL scenarios. Additionally, the question's theoretical nature may pose challenges in translating findings into practical applications.

### Critique of the Methodology
The paper's reliance on theoretical analysis may limit its applicability to real-world scenarios, where practical constraints and computational complexities could significantly impact the feasibility of constructing satisficing paths. Additionally, the extent to which theoretical findings are validated through empirical experiments or simulations is unclear, prompting a follow-up research about the practical relevance and robustness of theoretical results put forward.

### Critique of the Application Scenario
The focus on normal-form games may restrict the direct applicability of research findings to real-world MARL applications, which often involve more complex environments and dynamics. Furthermore, without concrete examples or case studies demonstrating the application of satisficing paths in real-world MARL problems, it's challenging to assess the practical significance of the research findings.

### Beyond Computer Science and Economics
- Interdisciplinary Connections: Insights from MARL research, particularly regarding the satisficing principle, could extend beyond computer science and economics. For example, they could inform the design of autonomous systems in various domains, such as cybersecurity and healthcare.
- Ethical Considerations: As MARL algorithms are deployed in real-world settings, addressing ethical concerns related to algorithmic fairness, transparency, and accountability becomes crucial. Future research could explore how the concept of satisficing paths intersects with these ethical considerations.

## Bibliography

Yongacoglu, B., Arslan, G., Pavel, L., & Yüksel, S. (2024, March 26). Paths to Equilibrium in Normal-Form Games. arXiv.org. https://arxiv.org/abs/2403.18079

Zhang, L. (Sunshine), Tian, X. (Michelle), Zhuang, Z., Zhang, L. (Sunshine), Tian, X. (Michelle), Wu, T. (Henry), Li, J., Wang, C. (Claire), Zhuang, Z. (2022). oTree Instructions for Behavioral Experiments. In Autumn 2021. https://doi.org/10.21428/aa21bfc0.841ff112

Zhang M., Zhang S., Yang Z., Chen L., Zheng J., Yang C., Li C., Zhou H., Niu Y., & Liu Y. (2023). GoBigger: A Scalable Platform for Cooperative-Competitive Multi-Agent Interactive Simulation. In The Eleventh International Conference on Learning Representations. https://openreview.net/forum?id=NnOZT_CR26Z
