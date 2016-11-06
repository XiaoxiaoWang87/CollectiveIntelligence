import recommendations

print recommendations.getRecommendations(recommendations.critics,'Toby')
print recommendations.getRecommendations(recommendations.critics,'Toby', similarity=recommendations.sim_distance)

movies=recommendations.transformPrefs(recommendations.critics)
print recommendations.topMatches(movies,'Superman Returns')
print recommendations.getRecommendations(movies,'Just My Luck')
