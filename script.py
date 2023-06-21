import csv
from google_play_scraper import app, reviews
# Specify the package name of the app 
app_package = 'com.app' 
# Get the app details
app_details = app(app_package)
# Fetch reviews for the app
result, continuation_token = reviews(
    app_package,
    lang='en',  # Language of the reviews (English)
    count=100,  # Number of reviews to fetch per page (max is 100)
)
# Open the CSV file in write mode
with open('reviews.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Rating', 'Content'])
    # Loop through the reviews
    while continuation_token:
        # Write the rating, content, and date of each review to the CSV file
        for review in result:
            rating = review['score']
            content = review['content']
            writer.writerow([rating, content])
        # Fetch the next page of reviews using the continuation token
        result, continuation_token = reviews(
            app_package,
            lang='en',
            count=100,
            continuation_token=continuation_token,
        )
