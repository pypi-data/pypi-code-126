import binpan

a = binpan.Exchange()

b = binpan.Wallet()

bb = b.spot_snapshot(startTime='2022-07-07 12:00:00')

c = binpan.handlers.wallet.daily_account_snapshot(account_type='SPOT', limit=7, time_zone='Europe/Madrid')

d = binpan.handlers.quest.get_exchange_limits()


print(a)
