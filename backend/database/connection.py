from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:@localhost/video_search_db"
engine = create_engine(DATABASE_URL)

