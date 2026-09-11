import random

situation = input("What's your situation?: ")

situation_lower = situation.lower()

category = None
if "school" in situation_lower or "class" in situation_lower or "homework" in situation_lower:
    category = "school"
elif "job" in situation_lower or "office" in situation_lower or "project" in situation_lower:
    category = "job"
elif "training" in situation_lower or "workout" in situation_lower: category = "training"

school_subjects = ["my dog", "my classmate", "an airplane"]
school_actions= ["ate my homework", "stole my homework", "flew my homework"]
school_consequences = ["now it's completely shredded", "my homework is gone", "my homework is in the air"]

job_subjects = ["my laptop", "the office Wi-Fi", "my manager"]
job_actions = ["crashed right before the deadline", "went down for hours", "moved the meeting last minute"]
job_consequences = ["so I lost all my progress", "so I couldn't submit anything", "so my whole schedule got thrown off"]

training_subjects = ["my gym bag", "a sudden leg cramp", "my workout playlist"]
training_actions = ["went missing right before I left", "hit me out of nowhere", "completely stopped working"]
training_consequences = ["so training was basically impossible", "so I had to lie down instead", "and I lost all motivation to go"]

if category == "school":
    subject = random.choice(school_subjects)
    action = random.choice(school_actions)
    consequence = random.choice(school_consequences)
elif category == "job":
    subject = random.choice(job_subjects)
    action = random.choice(job_actions)
    consequence = random.choice(job_consequences)
elif category == "training":
    subject = random.choice(training_subjects)
    action = random.choice(training_actions)
    consequence = random.choice(training_consequences)
else:
    subject = "something mysterious"
    action = "happened"
    consequence = "and that's all I know"

excuse = f"My excuse involves {subject} that {action}, {consequence}."
print(excuse)