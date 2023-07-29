link to the web app: https://booksrecommenderpy.herokuapp.com/

# books-recommendation
# In this book recommendation system, I made a model which will display top 5 recommended books for the user input.
Step 1: ( To display top 50 popular books on the initial dashboard)
1. Performed basic data exploration like null value check, duplicate check
2. Didn't perform EDA, since the main aim was to display the books on website.
3. There were 3 datasets ( books, users, ratings )
4. Merged the books dataset to rating dataset on ISBN number, since it was common to both.
5. Used groupby function on Book-Title and counted the no of ratings (by different users) received by each books and stored the book and rating data in num_rating_df.
6. Again used groupby on Book-Title but this time found the mean of all the ratings received each book and stored them in avg_rating_df.
7. Finally merged the avg_rating_df to num_rating_df on Book-Title, since we wanted unique book to have avg and num  of ratings and stored in popular_df dataset.
8. Then we filterd only top 50 books which had number of votes(ratings) greater than 250.
9. Modified the popular_df dataset by merging columns ['Book-Title','Book-Author','Image-URL-M','num_ratings','avg_ratings'] to it from the books dataset on Book-Title (since book-title is common to both)
10. Now the popular_df contains the columns ['Book-Title','Book-Author','Image-URL-M','num_ratings','avg_ratings'].


step 2: (for recommendation system)
1. Applied groupby function on User-ID and counted the number of votes received by the books  on the dataset (ratings_with_books )
2. This reduced the number of total users = 2,78,858 to only 92,106 who actually rated on any book.
3. Then stored the indices(User-ID) of all the users who voted on more than 200 books into padhe_likhe_users.
4. Used isin() function for pahde_likhe_users and filtered the rating_with_book on User-Id and stored them in filtered_rating dataset.
5. Now grouped the filtered rating dataset on Book-Title and counted the Book which recieved Ratings more than 50 times and called it famous_book.
6. Took the intersection of famous_books and filtered_rating on book-Title.
7. Created a pivot_table: "pivot_table=final_ratings.pivot_table(index='Book-Title',columns='User-ID',values='Book-Rating')"
8. The dimension of the pivot_table is 706*810 --> 706 are famous books(50+votes) and 810 are padhe_likhe_users(voted on more than 200 books)
9. Thus the pivot table contains the ratings of each user on each book.
10. Then found the similarity score of each books from other 706 books.
11. Found the 5 most similar books based on highest similarity score and stored them in similar_items.
12. Used for loop to iterate over the similar_items and appended (using extend) the book-title, author and image-url of similar books onto data[].


step 3: (pickle file)
1. Created a pickle file for popular books which will show the list of top 50 books on the inital dashboard.
2. Also created pickle file for books, similarity_score, and pivot_table since they were used in fetching data to the app.py file.


step 4: (app development)
1. Rendered the basic Flask template inside the app.py file.
2. Unpickled the popular.pkl to popular_df 
3. Created a route: @app.route('/') --> render_template(returned the index.html file and stored the book_name, author,votes,ratings,image-url from popular_df).
4. Now when the user visit the root URL '/' the function inside it will be executed and will return the "hello World" or the things we want to be there on the main dashboard. Firstly, it will take us to the index.html file and will render the content in it.
5. Then created two routes: @app.route('/recommend') and @app.route('/recommend_books',methods=['post']):
6. First will handle only the UI part, ie. will render the inital content like box to take input and a submit button.
7. Second route is to display the recommended books ie. handle the form submission.
8. When a user submits a form with a POST request to the /recommend_books URL, Flask will execute the recommend() function inside this route.
9. This function then retrieves the user input from the form using request.form.get('user_input').
10. Finally the recommend.html file will be rendered with the updated data and displyed to the users.
