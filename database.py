from sqlalchemy import create_engine,text


engine = create_engine("mysql+pymysql://jwmrks70zcp4ngm2eaef:pscale_pw_JAbhOzCmh02FtI47Kc65aOfohGyFOfFa2WgZCClO7oG@aws.connect.psdb.cloud/denshi",
                       connect_args={
                           "ssl":{
                               "ssl_ca":"/etc/ssl/cert.pem"
                           }
                       })

