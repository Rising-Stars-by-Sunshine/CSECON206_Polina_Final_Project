import random
from collections import Counter

def reach_consensus(preferences):
    vote_counts = Counter(preferences)
    max_votes = max(vote_counts.values())
    consensus = [preference for preference, count in vote_counts.items() if count == max_votes]
    return consensus

def update_preferences_beliefs(preferences, resources):
    posterior_beliefs = {preference: 0 for preference in resources}
    for preference in preferences:
        posterior_beliefs[preference] += 1
    total_counts = sum(posterior_beliefs.values())
    for preference in posterior_beliefs:
        posterior_beliefs[preference] /= total_counts
    return posterior_beliefs

def negotiate_allocation(resources, num_parties):
    all_preferences = {}
    for i in range(num_parties):
        preferences = {}
        for resource in resources:
            preference_rank = int(input(f"Party {i+1}, rank your preference for {resource} (1 being highest): "))
            preferences[resource] = preference_rank
        all_preferences[f"Party {i+1}"] = preferences

    final_preferences = {}
    for resource in resources:
        preferences_for_resource = {party: preferences[resource] for party, preferences in all_preferences.items()}
        consensus = max(preferences_for_resource, key=preferences_for_resource.get)
        final_preferences[consensus] = resource

    return final_preferences

def generate_random_projects(spheres):
    random_projects = {}
    for sphere, projects in spheres.items():
        random_project = random.choice(projects)
        random_funding = random.randint(10, 250) * 1000000  # Funding in millions
        random_projects[sphere] = {"project": random_project, "funding": random_funding}
    return random_projects

# Define spheres and projects
spheres = {
    "Economy": [
        "TradeNet Initiative", "BusinessBoost Project", "MarketEase Platform",
        "ExportPro Program", "CommerceConnect", "TradeAI Network",
        "GlobalGrowth Initiative", "MarketLink Project", "ExportEdge Program",
        "TradeTech Solutions"
    ],
    "Social Policy": [
        "CommunityCare Initiative", "HealthBridge Project", "EmpowerAll Program",
        "CommunityConnect Initiative", "WellnessHub Project", "CareCompass Program",
        "AidAccess Initiative", "HopeHarbor Project", "CommunitySupport Program",
        "EqualOpportunity Initiative"
    ],
    "Environment": [
        "EcoSmart Initiative", "GreenGrid Project", "EarthGuard Program",
        "EcoLife Initiative", "RenewaTech Project", "ClimateCare Program",
        "EcoBalance Initiative", "SustainaCity Project", "GreenPulse Program",
        "EcoCycle Initiative"
    ],
    "Culture": [
        "CulturEase Initiative", "ArtFusion Project", "HeritageLink Initiative",
        "CultureBridge Program", "UnityCanvas Initiative", "ArtisanCraft Project",
        "GlobalCultural Initiative", "TraditionsAlive Program", "CulturAware Initiative",
        "ArtisanConnect Program"
    ]
}

# Generate random projects
random_projects = generate_random_projects(spheres)

# Output the randomly generated projects
print("Good time of the day, dear party representatives.")
print("Our today's agenda is to determine where we are going to allocate funds for one of the next innovative projects.\n")
print("Here are the projects on our today's agenda:\n")
for sphere, project_info in random_projects.items():
    print(f"{sphere}:\n- Project: {project_info['project']}\n- Funding: (${project_info['funding'] // 1000000} Millions)\n")

# Use randomly generated projects in the negotiation process
resources = [project_info["project"] for project_info in random_projects.values()]
final_preferences = negotiate_allocation(resources, 3)
print("Bayesian probabilities before final choice:")
posterior_beliefs = update_preferences_beliefs(list(final_preferences.values()), resources)
for preference, probability in posterior_beliefs.items():
    print(f"{preference}: {probability:.2f}")
print("\nFinal allocation:", list(final_preferences.values())[0])
