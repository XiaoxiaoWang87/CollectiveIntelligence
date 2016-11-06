import recommendations

print recommendations.getRecommendations(recommendations.critics,'Toby')
print recommendations.getRecommendations(recommendations.critics,'Toby', similarity=recommendations.sim_distance)

movies=recommendations.transformPrefs(recommendations.critics)
print recommendations.topMatches(movies,'Superman Returns')
print recommendations.getRecommendations(movies,'Just My Luck')

itemsim=recommendations.calculateSimilarItems(recommendations.critics)
print itemsim


print recommendations.getRecommendedItems(recommendations.critics,itemsim,'Toby')
