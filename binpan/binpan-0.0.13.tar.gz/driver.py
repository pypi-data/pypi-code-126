import binpan

# MAS DE 100

# END_TIME
#
# # end_time coincidente con open ya cerrado
# btcusdt = binpan.Symbol(symbol='BTCUSDT',
#                         tick_interval='5m',
#                         end_time='2022-07-09 17:50:00',
#                         limit=2000,
#                         time_zone='Europe/Madrid',
#                         time_index=False)
# print(btcusdt.df)  # arreglao
#
# # end_time sin coincidir con open pero ya cerrado
# btcusdt = binpan.Symbol(symbol='BTCUSDT',
#                         tick_interval='5m',
#                         end_time='2022-07-09 17:49:00',
#                         limit=2000,
#                         time_zone='Europe/Madrid',
#                         time_index=False)
#
# print(btcusdt.df)  # viene perfecto
#
# # end_time futuro más de la vela actual coincidiendo con open
# btcusdt = binpan.Symbol(symbol='BTCUSDT',
#                         tick_interval='5m',
#                         end_time='2022-07-09 20:50:00',
#                         limit=2000,
#                         time_zone='Europe/Madrid',
#                         time_index=False)
# print(btcusdt.df)  # trae una vela de más si se pide algo ya cerrado
#
# # START_TIME
#
# # START_time coincidente con open ya cerrado
# btcusdt = binpan.Symbol(symbol='BTCUSDT',
#                         tick_interval='5m',
#                         start_time='2021-07-08 17:50:00',
#                         limit=2000,
#                         time_zone='Europe/Madrid',
#                         time_index=False)
# print(btcusdt.df)  #
#
# # START_time sin coincidir con open pero ya cerrado
# btcusdt = binpan.Symbol(symbol='BTCUSDT',
#                         tick_interval='5m',
#                         start_time='2021-06-09 17:49:00',
#                         limit=2000,
#                         time_zone='Europe/Madrid',
#                         time_index=False)
#
# print(btcusdt.df)  #

# # start_time con end_time futuro más de la vela actual coincidiendo con open
# btcusdt = binpan.Symbol(symbol='BTCUSDT',
#                         tick_interval='5m',
#                         start_time='2022-07-05 19:39:00',
#                         limit=2000,
#                         time_zone='Europe/Madrid',
#                         time_index=False)
# print(btcusdt.df)  # bien
#
# # sin starttime ni endtime pero con muchas velas mas de mil
# btcusdt = binpan.Symbol(symbol='BTCUSDT',
#                         tick_interval='5m',
#                         limit=2000,
#                         time_zone='Europe/Madrid',
#                         time_index=False)
# print(btcusdt.df)  #

# con start y con end
btcusdt = binpan.Symbol(symbol='BTCUSDT',
                        tick_interval='5m',
                        start_time='2022-07-05 19:39:00',
                        end_time='2022-07-09 19:39:00',
                        limit=2000,
                        time_zone='Europe/Madrid',
                        time_index=False)
print(btcusdt.df)  #

exit()
