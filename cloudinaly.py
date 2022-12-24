import cloudinary
import cloudinary.uploader

cloudinary.config(
  cloud_name = "dv2q2aczs",
  api_key = "323881737694222",
  api_secret = "SJ1COcW-Z7DcRP4vQBwvYZjDdqs"
)

uploaddata = cloudinary.uploader.upload("skirt.jpg",
  detection = "cld-fashion", auto_tagging = 0.6, )

tag = uploaddata["tags"][0]
print(tag)
attributesdata = uploaddata["info"]["detection"]["object_detection"]['data']["cld-fashion"]["tags"][tag][0]["attributes"]

if "sleeve length" in attributesdata:
  length = attributesdata["sleeve length"][0][0]
  print(length)
elif "leg length" in attributesdata:
  length = attributesdata["leg length"][0][0]
  print(length)
elif "skirt length" in attributesdata:
  length = attributesdata["skirt length"][0][0]
  print(length)
else:
  length = "none"
  print("can't get length")

seasonev = "none"

if length in ["mini","short","above the knee"]:
  seasonev = "short"
elif length in ["knee","below the knee","3/4 cropped","elbow"]:
  seasonev = "midium"
elif length in ["7/8 cropped","three quarter","midi"]:
  seasonev =  "semilong"
elif length in ["full","maxi","long (wrist)"]:
  seasonev = "long"
else:
  seasonev = "nosleaves"

print(seasonev)