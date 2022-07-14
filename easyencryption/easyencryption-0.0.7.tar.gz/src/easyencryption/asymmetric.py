import rsa

async def genkeys():
    publickey, privatekey = rsa.newkeys(512)
    keys = [publickey, privatekey]
    print(type(publickey))
    print(publickey)
    print(type(privatekey))
    print(privatekey)
    with open("pubeasyencryption.key", "wb") as pub_key_file:
        pub_key_file.write(publickey)
    with open("priveasyencryption.key", "wb") as priv_key_file:
        priv_key_file.write(privatekey)
    return keys

async def regenkeys():
    if os.path.exists("pubeasyencryption.key"):
        os.remove("pubeasyencryption.key")
    if os.path.exists("priveasyencryption.key"):
        os.remove("priveasyencryption.key")
    await genkey()

async def callpubkey():
  try:
    key = open("pubeasyencryption.key", "rb").read()
    if str(key) == "b''":
      await genkeys()
      key = open("pubeasyencryption.key", "rb").read()
    return key
  except:
    await genkeys()
    key = open("pubeasyencryption.key", "rb").read()
    return key

async def callprivkey():
  try:
    key = open("priveasyencryption.key", "rb").read()
    if str(key) == "b''":
      await genkeys()
      key = open("priveasyencryption.key", "rb").read()
    return key
  except:
    await genkeys()
    key = open("priveasyencryption.key", "rb").read()
    return key

async def asymencrypt(slogan):
  key = await callpubkey()
  coded_slogan = rsa.encrypt(slogan.encode(), publickey)
  return coded_slogan

async def asymdecrypt(coded_slogan):
  key = await callprivkey()
  decoded_slogan = rsa.decrypt(coded_slogan, privatekey).decode()
  decoded_slogan = str(decoded_slogan)
  decoded_slogan = decoded_slogan[2:]
  decoded_slogan = decoded_slogan[:-1]
  return(decoded_slogan)

