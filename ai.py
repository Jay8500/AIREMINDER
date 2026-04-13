# 1. IMPORT the building blocks
from sklearn import tree

# 2. PREPARE DATA (The "Features")
# [Weight in grams, Texture (1=Smooth, 0=Bumpy)]
features = [[140, 1], [130, 1], [150, 0], [170, 0]]

# 3. LABELS (The "Targets")
# 0 = Apple, 1 = Orange
labels = [0, 0, 1, 1]

# 4. CHOOSE THE ALGORITHM (The "Engine")
# We use a Decision Tree: it learns by asking Yes/No questions
classifier = tree.DecisionTreeClassifier()

# 5. TRAINING (The "Learning" phase)
# The AI looks for patterns between features and labels
classifier = classifier.fit(features, labels)

# 6. PREDICTION (The "Test")
# Let's give it a new fruit: 160g and Bumpy (0)
result = classifier.predict([[160, 0]])

if result[0] == 0:
    print("AI says: It's an Apple!")
else:
    print("AI says: It's an Orange!")