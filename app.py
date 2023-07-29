from flask import Flask, render_template,request

import numpy as np
#importing the pkl file
import pickle
# this pkl file simply contains the top 50- popular books data
popular_df  = pickle.load(open('popular.pkl','rb'))

# these files contains the data for the recommendation system
pivot_table = pickle.load(open('pivot_table.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_score=pickle.load(open('similarity_score.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    # sending all the columns data to the index.html page
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                            author=list(popular_df['Book-Author'].values),
                            votes=list(popular_df['num_ratings'].values),
                            rating=np.round(list(popular_df['avg_ratings'].values),2),
                            image_url=list(popular_df['Image-URL-M'].values) 
                            )
  
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    #fetch the index of book-name
    index = np.where(pivot_table.index==user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1],reverse=True)[1:6]
    
    # now we got the similar_items(which has book-index and score), so will loop into it to print them.
    # using append makes the list 2-D list
    data=[]
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pivot_table.index[i[0]]]
        item.extend(temp_df.drop_duplicates('Book-Title')['Book-Title'].values)
        item.extend(temp_df.drop_duplicates('Book-Title')['Book-Author'].values)
        item.extend(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values)
        
        data.append(item)
    print(data)
    return render_template('recommend.html', data=data)

if __name__ == '__main__': 
    app.run(debug=True)