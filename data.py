from classes import *

Jackera = LearningPlatform("Jackera")

Algebra1 = Course("Algebra 1", "Equations, functions, graphs, problem-solving.", "Math", "Beginner")
Biology = Course("Biology", "Life, cells, genetics, ecosystems, evolution.", "Science", "Intermediate")
Chemistry = Course("Chemistry", "Matter, atoms, reactions, periodic trends, bonding.", "Science", "Intermediate")
Spanish1 = Course("Spanish 1", "Language, culture, communication, grammar, conversation.", "Language", "Beginner")
History1 = Course("History 1", "Civilizations, cultures, events, leaders, revolutions.", "Social Studies", "Beginner")
Geometry = Course("Geometry", "Shapes, theorems, proofs, trigonometry, and measurement.", "Math", "Intermediate")
Calculus = Course("Calculus", "Limits, derivatives, integrals, and applications of continuous change.", "Math", "Advanced")

Alg1_L1 = Lesson("Algebra Foundations", "Video", 30, "Overview and History of Algebra")
Alg1_L2 = Lesson("Solving Equations & Inequalities", "Text", 60, "Algebraic Equations and Inequalities")
Alg1_L3 = Lesson("Working with Units", "Interactive", 60, "Rate Conversion")
Alg1_L4 = Lesson("Linear Equations & Graphs", "Text", 60, "Two-variable Linear Equations Intro")
Alg1_L5 = Lesson("Forms of Linear Equations", "Video", 60, "Intro to Linear Equation Forms")
Alg1_L6 = Lesson("Systems of Equations", "Text", 60, "Solving Systems of Equations")

Geo_L1 = Lesson("Introduction to Geometry", "Video", 30, "Points, Lines, Planes, and Angles")
Geo_L2 = Lesson("Triangles and Their Properties", "Text", 60, "Classifying Triangles and Angle Sums")
Geo_L3 = Lesson("Congruence and Similarity", "Interactive", 60, "Transformations and Proofs of Congruence")
Geo_L4 = Lesson("Polygons and Quadrilaterals", "Text", 60, "Properties of Parallelograms, Trapezoids, and Other Polygons")
Geo_L5 = Lesson("Circles", "Video", 60, "Chords, Tangents, Arcs, and Central Angles")
Geo_L6 = Lesson("Perimeter, Area, and Volume", "Text", 60, "Measuring 2D and 3D Shapes")
Geo_L7 = Lesson("Coordinate Geometry", "Interactive", 60, "Slopes, Midpoints, and Distance Formula")
Geo_L8 = Lesson("Trigonometry in Geometry", "Video", 60, "Right Triangles, Sine, Cosine, and Tangent")
Geo_L9 = Lesson("Geometric Proofs", "Text", 60, "Two-Column Proofs and Reasoning with Theorems")
Geo_L10 = Lesson("Transformations", "Interactive", 60, "Reflections, Rotations, Translations, and Dilations")

Calc_L1 = Lesson("Introduction to Calculus", "Video", 30, "Understanding Limits and the Concept of Change")
Calc_L2 = Lesson("Limits and Continuity", "Text", 60, "Evaluating Limits and Identifying Continuity")
Calc_L3 = Lesson("Derivatives Basics", "Interactive", 60, "Definition of the Derivative and First Principles")
Calc_L4 = Lesson("Rules of Differentiation", "Audio", 60, "Power Rule, Product Rule, Quotient Rule, and Chain Rule")
Calc_L5 = Lesson("Applications of Derivatives", "Video", 60, "Tangent Lines, Velocity, and Optimization Problems")
Calc_L6 = Lesson("Graphing with Derivatives", "Interactive", 60, "Concavity, Inflection Points, and Curve Sketching")
Calc_L7 = Lesson("Introduction to Integration", "Audio", 60, "Antiderivatives and the Indefinite Integral")
Calc_L8 = Lesson("Definite Integrals", "Text", 60, "Area Under Curves and the Fundamental Theorem of Calculus")
Calc_L9 = Lesson("Techniques of Integration", "Interactive", 60, "Substitution, Integration by Parts, and Partial Fractions")
Calc_L10 = Lesson("Applications of Integrals", "Video", 60, "Volumes, Work, and Accumulated Change in Context")

Bio_L1 = Lesson("Intro to Biology", "Video", 30, "The Science of Biology")
Bio_L2 = Lesson("Waters, Acids, and Bases", "Video", 60, "Adhesion and Cohesion")
Bio_L3 = Lesson("Macromolecules", "Video", 60, "Intro to Macromolecules")
Bio_L4 = Lesson("Energy and Enzymes", "Text", 60, "Laws of Thermodynamics")
Bio_L5 = Lesson("Structure of a Cell", "Video", 60, "Intro to Cells")
Bio_L6 = Lesson("Membranes and Transport", "Interactive", 60, "Cell Membranes")

Chem_L1 = Lesson("Introduction to Chemistry", "Video", 45, "Atoms and Elements Overview")
Chem_L2 = Lesson("The Periodic Table", "Text", 60, "Understanding groups, periods, and element properties")

Span1_L1 = Lesson("Introduction to Spanish", "Video", 30, "Spanish Alphabet and Pronunciation")
Span1_L2 = Lesson("Basic Greetings & Expressions", "Text", 45, "Common Phrases and Everyday Conversation")
Span1_L3 = Lesson("Numbers and Days", "Text", 45, "Counting and Calendar Basics")

His1_L1 = Lesson("Introduction to History", "Video", 30, "Understanding the study of history and its importance")
His1_L2 = Lesson("Ancient Civilizations", "Audio", 45, "Exploring Mesopotamia, Egypt, and early societies")
His1_L3 = Lesson("Classical Empires", "Interactive", 45, "Overview of Greece, Rome, and their lasting influence")


Bio_L1_Q1 = Question("Which of the following best describes the primary focus of biology?",
                    ["A) The study of chemical reactions in the lab", "B) The study of celestial objects and their movements", "C) The study of life and living organisms", "D) The study of physical forces like motion and energy"],
                    "C")