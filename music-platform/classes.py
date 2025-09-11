from datetime import timedelta
import datetime
import random
import time

class Song:
    def __init__(self, title, artist, album, duration_seconds, genre, release_year):
        self.title = title
        self.artist = artist # Always a list
        self.album = album
        self.duration_seconds = duration_seconds
        self.genre = genre
        self.release_year = release_year
        self.play_count = 0
        self.likes = 0
        self.audio_quality = None
        self.tags = []
    
    # def __str__(self):
    #     # Join multiple artists into one string
    #     artists_str = ", ".join(self.artist)
    #     return f"{self.title} by {artists_str}"
    
    def is_similar_to(self, other_song):
        score = 0
        if self.genre == other_song.genre:
            score += 0.5
        for tag in self.tags:
            if tag in other_song.tags:
                score += 0.15
        for artist in self.artist:
            if artist in other_song.artist:
                score += 0.15
        if score > 1:
            return 1.0
        else:
            return score
        
        # print(Jackify.songs[( "Green Day", "Holiday" )].is_similar_to(
        # Jackify.songs[( "Muse", "Hysteria" )]))

    
    def get_duration_formatted(self):
        minutes = self.duration_seconds // 60
        seconds = self.duration_seconds % 60
        return f"{minutes:02}:{seconds:02}"

        # for song in Jackify.artists["Muse"].albums["Absolution"].songs:
        #     print(song.get_duration_formatted())

class Artist:
    def __init__(self, name, bio, genres):
        self.name = name
        self.bio = bio
        self.genres = genres
        self.songs = []
        self.followers = []
        self.monthly_listeners = 0
        self.albums = {}
    
    def add_album(self, album):
        self.albums[album.title] = album

        # Jackify.artists["Muse"].add_album(Absolution)
    
    def get_top_songs(self, limit=10):
        top_songs = sorted(self.songs, key=lambda song: song.likes + song.play_count, reverse=True)
        return top_songs[:limit]

        # Muse_Intro.likes = 5
        # Muse_Intro.play_count = 7

        # Muse_Hysteria.likes = 61
        # Muse_Hysteria.play_count = 6

        # for song in Muse.get_top_songs():
        #     print(song.title)
            
    
    def get_total_plays(self):
        total_plays = 0
        for song in self.songs:
            total_plays += song.play_count
        return total_plays

        # Jackify.users["Jack"].play_song(DrakeFuture_DigitalDash)
        # print(Jackify.artists["Drake"].get_total_plays())
    
    def get_collaboration_artists(self):
        collaborators = set()
        for song in self.songs:
            for artist_name in song.artist:
                if artist_name != self.name:
                    collaborators.add(artist_name)
        return list(collaborators)
    
        # print(Jackify.artists["Drake"].get_collaboration_artists())

class Album:
    def __init__(self, title, artist, release_date, album_type):
        self.title = title
        self.artist = artist # Always a list
        self.release_date = release_date
        self.album_type = album_type
        self.songs = []
        self.ratings = [] # Stores tuples (user, rating)
        self.cover_art_url = None
        self.total_duration = 0
    
    def add_song(self, song):
        self.songs.append(song)
        for album_artist in self.artist:
            if album_artist.name not in song.artist:
                song.artist.append(album_artist.name)

        # Jackify.artists["Muse"].albums["Absolution"].add_song(Muse_Hysteria)
    
    def get_average_rating(self):
        if len(self.ratings) == 0:
            return None
        total_rating = 0
        for user, rating in self.ratings:
            total_rating += rating
        return round(total_rating / len(self.ratings))

        # print(Jackify.artists["Green Day"].albums["American Idiot"].get_average_rating())
    
    def calculate_total_duration(self):
        total = 0
        for song in self.songs:
            total += song.duration_seconds
        self.total_duration = total

        # Jackify.artists["Green Day"].albums["American Idiot"].calculate_total_duration()
        # print(Jackify.artists["Green Day"].albums["American Idiot"].total_duration)

class User:
    def __init__(self, username, email, subscription_type):
        self.username = username
        self.email = email
        self.subscription_type = subscription_type
        self.playlists = {}
        self.listening_history = []
        self.liked_songs = []
        self.following_artists = []
        self.rated_albums = {}
        self.listening_preferences = {}
        self.current_streak = 0
        self.subscription_end_date = None
    
    def follow(self, artist):
        if self not in artist.followers:
            artist.followers.append(self)

        # Jackify.users["Jack"].follow(Drake)
        # for follower in Jackify.artists["Drake"].followers:
        #     print(follower.username)
    
    def unfollow(self, artist):
        if self in artist.followers:
            artist.followers.remove(self)
        
        # Jackify.users["Jack"].unfollow(Drake)

    def play_song(self, song):
        print(f"Playing {song.title}")
        time.sleep(0.1)
        self.listening_history.append((song, datetime.datetime.now()))
        song.play_count += 1
        if len(self.listening_history) % 3 == 0:
            print("Ad")
            time.sleep(0.25)
        if song.genre not in self.listening_preferences:
            self.listening_preferences[song.genre] = 1
        else:
            self.listening_preferences[song.genre] += 1
        
        # Jackify.users["Jack"].play_song(Muse_Hysteria)
        # Jackify.users["Jack"].play_song(DrakeFuture_DigitalDash)
        # Jackify.users["Jack"].play_song(DrakeFuture_ImThePlug)
        # Jackify.users["Jack"].play_song(DrakeFuture_Scholarships)
        # Jackify.users["Jack"].play_song(GreenDay_AmericanIdiot)
        # for song, timestamp in Jackify.users["Jack"].listening_history:
        #     print(f"{song.title} played at {timestamp}")
        # print(Jackify.songs[Muse_Hysteria.title].play_count)
        # print(Jackify.users["Jack"].listening_preferences)
    
    def rate_album(self, album, rating):
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5.")
            # Raises a ValueError if value isn't between 1-5 or is not an int
        if album in self.rated_albums:
            self.rated_albums[album] = rating
            for i, (user, old_rating) in enumerate(album.ratings):
                if user == self:
                    album.ratings[i] = (self, rating)
                    break
        else:
            self.rated_albums[album] = rating
            album.ratings.append((self, rating))

        # Jackify.users["Jack"].rate_album(AmericanIdiot, 5)
        # Jackify.users["Jack"].rate_album(AmericanIdiot, 3)
        # Jackify.users["Lola"].rate_album(AmericanIdiot, 5)

        # for album, rating in Jackify.users["Jack"].rated_albums.items():
        #     print(album.title, rating)

        # for user, rating in Jackify.artists["Green Day"].albums["American Idiot"].ratings:
        #     print(user.username, rating)   
    
    def like_song(self, song):
        if song in self.liked_songs:
            pass
        else:
            self.liked_songs.append(song)
            song.likes += 1
        
        # Jackify.users["Jack"].like_song(Muse_Hysteria)
        # print(Jackify.songs["Muse", "Hysteria"].likes)

    def create_playlist(self, name, is_public, description=""):
        if name in self.playlists:
            pass
        else:
            self.playlists[name] = Playlist(name, self, is_public, description)

        # Jackify.users["Jack"].create_playlist("Jack's Playlist", True, "Description")
    
    def get_listening_time_today(self):
        total_seconds_today = 0
        today = datetime.date.today()
        for song, timestamp in self.listening_history:
            if timestamp.date() == today:
                total_seconds_today += song.duration_seconds
        return total_seconds_today
        
        # print(Jackify.users["Jack"].get_listening_time_today())
    
    def get_favorite_genres(self):
        genres_list = []
        for genre, plays in self.listening_preferences.items():
            genres_list.append((genre, plays))
        genres_list.sort(key=lambda genres: genres[1], reverse=True)
        return [genre for genre, plays in genres_list[:3]]

        # print(Jackify.users["Jack"].get_favorite_genres())
    
    def get_discovery_score(self):
        unique_songs = set()
        song_history = set()
        recent_10 = self.listening_history[-10:]
        all_but_recent_10 = self.listening_history[:-10]
        for (song, _) in (all_but_recent_10):
            song_history.add(song)
        for (song, _) in (recent_10):
            if song not in song_history:
                unique_songs.add(song)
        return len(unique_songs) / len(recent_10) if recent_10 else 0.0

        # print(Jackify.users["Jack"].get_discovery_score())

        # Should increase 10 to 100 or 1000 for practical use
    
    def subscribe(self):
        self.subscription_type = "premium"
        self.subscription_end_date = datetime.now() + timedelta(days=30)

        # print(Jackify.users["Jack"].subscription_type)
        # Jackify.users["Jack"].subscribe()
        # print(Jackify.users["Jack"].subscription_type)

    def check_subscription_status(self):
        if self.subscription_type == "premium" and datetime.now() > self.subscription_end_date:
            self.subscription_type = "free"
            self.subscription_end_date = None

        # Jackify.users["Jack"].check_subscription_status()

class Playlist:
    def __init__(self, name, creator, is_public, description):
        self.name = name
        self.creator = creator
        self.is_public = is_public
        self.description = description
        self.songs = []
        self.followers = []
        self.creation_date = datetime.datetime.now()
        self.total_duration = 0
        self.last_modified = None
        self.is_collaborative = False

    def add_song(self, song, position=None):
        self.songs.append(song)

        # Jackify.users["Jack"].playlists["Jack's Playlist"].add_song(Muse_Hysteria)
        # Jackify.users["Jack"].playlists["Jack's Playlist"].add_song(GreenDay_Holiday)

        # for name, playlist in Jackify.users["Jack"].playlists.items():
        #     print(name)
        #     for char in range(len(name)):
        #         print("-", end="")
        #     print()
        #     for song in playlist.songs:
        #         print(song.title)
    
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

        # Jackify.users["Jack"].playlists["Jack's Playlist"].remove_song(GreenDay_Holiday)
    
    def shuffle(self):
        shuffled_playlist_songs = list(self.songs)
        random.shuffle(shuffled_playlist_songs)
        return shuffled_playlist_songs

        # for song in Jackify.users["Jack"].playlists["Jack's Playlist"].shuffle():
        #     print(song.title)
        
    
    def get_total_duration(self):
        total = 0
        for song in self.songs:
            total += song.duration_seconds
        self.total_duration = total

        # Jackify.users["Jack"].playlists["Jack's Playlist"].get_total_duration()
        # print(Jackify.users["Jack"].playlists["Jack's Playlist"].total_duration)
    
    def get_mood_analysis(self):
        excited = ["energetic", "uplifting", "confident", "rebellious"]
        emotional = ["melancholy", "nostalgic", "emotional"]
        intense = ["dark", "aggressive", "anxious", "intense"]
        relaxed = ["peaceful", "dreamy", "ambient", "relaxed"]
        dramatic = ["dramatic", "epic", "mysterious", "romantic"]
        tags_dict = {}
        moods_dict = {"Excited": 0, "Emotional": 0, "Intense": 0, "Relaxed": 0, "Dramatic": 0}
        for song in self.songs:
            for tag in song.tags:
                if tag not in tags_dict:
                    tags_dict[tag] = 1
                else:
                    tags_dict[tag] += 1
        for tag, amount in tags_dict.items():
            if tag in excited:
                moods_dict["Excited"] += amount
            elif tag in emotional:
                moods_dict["Emotional"] += amount
            elif tag in intense:
                moods_dict["Intense"] += amount
            elif tag in relaxed:
                moods_dict["Relaxed"] += amount
            elif tag in dramatic:
                moods_dict["Dramatic"] += amount
        return max(moods_dict, key=moods_dict.get)

        # print(Jackify.users["Jack"].playlists["Jack's Playlist"].get_mood_analysis())

    
    def set_collaborative(self, collaborative=True):
        self.is_collaborative = collaborative
    
    def update_playlist_privacy(self):
        if self.is_public == True:
            self.is_public = False
        else:
            self.is_public = True
        
        # Jackify.users["Jack"].playlists["Jack's Playlist"].update_playlist_privacy()

class StreamingService:
    def __init__(self, service_name):
        self.service_name = service_name
        self.users = {}
        self.songs = {}
        self.artists = {}
        self.albums = {}
        self.trending_songs = []
    
    def register_user(self, username, email, subscription_type):
        self.users.update({username:User(username, email, subscription_type)})

        # Jackify.register_user("Jack", "jhohman@gmail.com", "free")
        # Jackify.register_user("Lola", "lhohman@gmail.com", "free")

        # for username, user in Jackify.users.items():
        #     print(username)
    
    def add_artist(self, artist):
        self.artists.update({artist.name:artist})

        # Jackify.add_artist(Muse)
        # for name, artist in Jackify.artists.items():
        #     print(name)
    
    def add_album(self, album):
        self.albums[album.title] = album
        for artist in album.artist:
            if artist.name in self.artists:
                self.artists[artist.name].add_album(album)
    
    def add_song(self, song):
        for artist_name in song.artist:   # song.artist is a list of names
            artist = self.artists.get(artist_name)
            if artist and song not in artist.songs:
                artist.songs.append(song)
            self.songs[(artist_name, song.title)] = song
        
        # Jackify.add_song(Muse_Hysteria, Muse)
        # Jackify.add_song(Muse_Blackout, Muse)

        # for title, song in Jackify.songs.items():
        #     print(title)
        
    def get_song_popularity_score(self, song):
        total_weighted_score = 0
        for user in self.users.values():
             for song_tuple in user.listening_history:
                if song_tuple[0] == song:
                    days_ago = (datetime.datetime.now() - song_tuple[1]).days
                    weight = 0.5 ** (days_ago / 7)
                    total_weighted_score += weight
        popularity_score = (0.2 * song.likes) + (0.7 * total_weighted_score) + (0.1 * song.play_count)
        return popularity_score

        # print(Jackify.get_song_popularity_score(Muse_Hysteria))
    
    def album_get_most_popular_song(self, album):
        songs_with_popularity = []
        for song in album.songs:
            songs_with_popularity.append((song, self.get_song_popularity_score(song)))
        songs_with_popularity.sort(key=lambda song: song[1], reverse=True)
        return songs_with_popularity[0][0]

        # print(Jackify.album_get_most_popular_song(Absolution).title)
    
    def get_trending_artists(self):
        artist_plays = {}
        trending_artists = []
        for user in self.users.values():
            for song, timestamp in user.listening_history:
                if (datetime.datetime.now() - timestamp).days <= 7:
                    for artist in song.artist:
                        if artist not in artist_plays:
                            artist_plays[artist] = 1
                        else:
                            artist_plays[artist] += 1
        for artist, plays in artist_plays.items():
            trending_artists.append((artist, plays))
        trending_artists.sort(key=lambda x: x[1], reverse=True)
        return trending_artists[:3]

        # trending_artists = Jackify.get_trending_artists()
        # for artist in trending_artists:
        #     print(artist[0])

        # or print(Jackify.artists[artist[0]])
                
    
    def search(self, query, search_type="all"):
        results = []
        seen = set()
        if search_type == "users":
            for user in self.users:
                if query.lower() in user.lower():
                    results.append(user)
        elif search_type == "songs":
            for _, song in self.songs.items():
                if query.lower() in song.title.lower():
                    if song not in seen:
                        results.append(song.title)
                        seen.add(song)
        elif search_type == "artists":
            for artist in self.artists:
                if query.lower() in artist.lower():
                    results.append(artist)
        elif search_type == "albums":
            for album in self.albums:
                if query.lower() in album.lower():
                    results.append(album)
        else:
            for user in self.users:
                if query.lower() in user.lower():
                    results.append(user)
            for _,  song in self.songs.items():
                if query.lower() in song.title.lower():
                    if song not in seen:
                        results.append(song.title)
                        seen.add(song)
            for artist in self.artists:
                if query.lower() in artist.lower():
                    results.append(artist)
            for album in self.albums:
                if query.lower() in album.lower():
                    results.append(album)
        return results

        # print(Jackify.search("lu", search_type="all"))
    
    def get_recommendations_for_user(self, user, count=20):
        target_history = set(song for song, _ in user.listening_history)
        similar_users = []
        recommended = set()
        for other_user in self.users.values():
            if other_user == user:
                continue
            other_history = set(song for song, _ in other_user.listening_history)
            overlap = len(target_history & other_history)
            if overlap > 0:
                similar_users.append((overlap, other_user))
        similar_users.sort(reverse=True, key=lambda x: x[0])
        for _, other_user in similar_users:
            for song, _ in other_user.listening_history:
                if song not in target_history:
                    recommended.add(song)
                if len(recommended) >= count:
                    break
            if len(recommended) >= count:
                break
        return list(recommended)[:count]
    
        # print(Jackify.get_recommendations_for_user(Jackify.users["Jack"]))

    def get_trending_songs(self):
        song_plays = {}
        trending_songs = []
        for user in self.users.values():
            for song, timestamp in user.listening_history:
                if (datetime.datetime.now() - timestamp).days <= 7:
                    if song not in song_plays:
                        song_plays[song] = 1
                    else:
                        song_plays[song] += 1
        for song, plays in song_plays.items():
            trending_songs.append((song, plays))
        trending_songs.sort(key=lambda x: x[1], reverse=True)
        return trending_songs[:3]

        # trending_songs = Jackify.get_trending_songs()
        # for song in trending_songs:
        #     print(song[0].title)
    
    def generate_radio_station(self, seed_song):
        station_songs = []
        same_genre_songs = []
        same_tag_songs = []
        seen = set()
        played = set()
        played.add(seed_song)
        for song in self.songs.values():
            if song.genre == seed_song.genre and song not in seen:
                same_genre_songs.append(song)
                seen.add(song)
            for tag in song.tags:
                if tag in seed_song.tags and song not in seen:
                    same_tag_songs.append(song)
                    seen.add(song)
        for song in same_genre_songs:
            for tag in song.tags:
                if tag in seed_song.tags and song not in played:
                    station_songs.append(song)
                    played.add(song)
        for song in same_genre_songs:
            if song not in played:
                station_songs.append(song)
        for song in same_tag_songs:
            if song not in played:
                station_songs.append(song)
        return station_songs

        # radio_station = Jackify.generate_radio_station(Muse_Hysteria)
        # for song in radio_station:
        #     print(song.title)

    # Hysteria is alt rock and has tags energetic and intense
    def get_user_wrapped(self, user, year):
        played_songs = {}
        user_wrapped = []
        for song, timestamp in user.listening_history:
            if timestamp.year == year:
                if song not in played_songs:
                    played_songs[song] = 1
                else:
                    played_songs[song] += 1
        for song, plays in played_songs.items():
            user_wrapped.append((song, plays))
        user_wrapped.sort(key=lambda song: song[1], reverse=True)
        return user_wrapped[:100]

        # print(Jackify.get_user_wrapped(Jackify.users["Jack"], 2025))

    def calculate_artist_royalties(self, artist):
        dollars = 0
        for song in artist.songs:
            dollars += song.play_count * (0.008 / len(song.artist))
        return round(dollars, 2)

        # print(Jackify.calculate_artist_royalties(GreenDay))