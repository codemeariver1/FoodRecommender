from restaurants.restaurants import Restaurants

# inst = Restaurants()
# inst.land_first_page()
try:
    with Restaurants() as bot:
        bot.land_first_page()
        bot.search_nearby_restaurants()
        bot.apply_filtrations()
        bot.report_results()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            "You are trying to run the FoodRecommender bot from the command line\n"
            "Please add your Selenium Driver to PATH \n"
            "Windows: \n"
            "   set PATH=%PATH%;C:\path-to-your-folder\ \n\n"
            "Mac or Linux: \n"
            "   PATH=$PATH:/path/toyour/folder/ \n"
        )
    else:
        raise
