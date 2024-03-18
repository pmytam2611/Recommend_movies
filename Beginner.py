import pandas as pd
#Load the Movies data
movies = pd.read_csv('ml-100k/u.item', sep="|", encoding='latin-1', header=None)
movies.columns = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action',
                'Adventure', 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 
                'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

# Tìm kiếm phim có tên "The Shawshank Redemption"
phim_tim_kiem = movies[movies["title"].str.contains("The Shawshank Redemption")]

# In thông tin phim
print(phim_tim_kiem)
