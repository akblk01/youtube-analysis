import pandas as pd

df = pd.read_csv("DEvideos.csv")

# Bring the first 10 records.
result = df.head(10)
print(result)

# Bring the second 5 records.
result = df[5:20].head(5)

# Find the column names in the data set.
result = df.columns
print(result)

# Delete some columns below and list the remaining columns.
result = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1, inplace=True)
print(result)

# Find the average of the likes and dislikes.

result = df["likes"].mean()
print(result)

result = df["dislikes"].mean()
print(result)

# Bring the like and dislike columns of the first 50 videos.
result = df[["likes","dislikes"]]
print(result)

# Which is the most viewed video?
result = df[df["views"].max() == df["views"]]["title"].iloc[0]
print(result)

# Which is the least viewed video?
result = df[df["views"].min() == df["views"]]["title"].iloc[0]
print(result)

# What are the top 10 most viewed videos?
result = df.sort_values("views", ascending=False).head(10)[["title","views"]]
print(result)

# Bring the average of likes according to the category in order.
result = df.groupby("category_id").mean().sort_values("likes")["likes"]
print(result)

# Rank the number of comments by category from top to bottom.
result = df.groupby("category_id").sum().sort_values("comment_count", ascending = False)["comment_count"]
print(result)

# How many videos are in each category?
result = df.groupby("category_id")["video_id"].count()
print(result)

# Show the title length information of each video in a new column.
df["len_title"] = df["title"].apply(len)

# Show the number of tags used for each video in the new column.
df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))


# List the most popular videos (by like/dislike ratio)
def likedislikeoranhesapla(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList))

    oranListesi = []

    for like,dislike  in liste:
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi

df["beğeni_orani"] = likedislikeoranhesapla(df)

print(df.sort_values("beğeni_orani",ascending=False)[["title","likes","dislikes","beğeni_orani"]])
