
# text_to_speech_gTTS.py -
# text-to-speech from English and Thai text 
# Burmese text not as clear  
# Install: 
# https://www.codingem.com/python-text-to-speech/
# https://www.geeksforgeeks.org/convert-text-speech-python/


from gtts import gTTS
import os

mytext = """ 
ภูเก็ตเป็นวันที่ร้อนและชื้น และแสงแดดก็สาดส่องลงมาบนถนนที่พลุกพล่าน แต่ซาร่าห์ก็ไม่รังเกียจความร้อน เธอตื่นเต้นเกินกว่าจะได้ดำน้ำในหมู่เกาะสิมิลันที่สวยงาม
ซาร่าห์หลงใหลในท้องทะเลมาโดยตลอด และเธอก็ใฝ่ฝันที่จะได้สำรวจน้ำทะเลใสราวคริสตัลของเกาะสิมิลันตราบเท่าที่เธอจำได้ ในที่สุดเมื่อเธอมีโอกาสได้ไปดำน้ำบนเรือแบบสดบนเรือที่เกาะต่างๆ เธอจึงรีบคว้าโอกาสนั้นไว้

เรือดำน้ำที่มีชีวิตบนเรือมีขนาดเล็กและสะดวกสบาย มีพื้นที่เพียงพอสำหรับนักดำน้ำ 6 คนและลูกเรือ Sarah ผูกมิตรกับนักดำน้ำคนอื่นๆ ได้อย่างรวดเร็ว ซึ่งล้วนแต่เป็นทหารผ่านศึกที่ช่ำชองและผ่านการดำน้ำมาแล้วหลายร้อยครั้ง

ขณะที่พวกเขาล่องเรือไปยังเกาะสิมิลัน ซาร่าห์อดไม่ได้ที่จะรู้สึกตื่นเต้นและคาดหวังในตัวเธอ เธอเคยได้ยินมาว่าหมู่เกาะสิมิลันเป็นที่ตั้งของแนวปะการังที่สวยงามที่สุดในโลก และเธออดใจรอไม่ไหวที่จะได้เห็นพวกมันด้วยตัวเธอเอง

ในที่สุด หลังจากสิ่งที่ดูเหมือนชั่วนิรันดร์ พวกเขาก็มาถึงจุดดำน้ำจุดแรก ซาร่าห์และนักประดาน้ำคนอื่นๆ สวมอุปกรณ์และเตรียมลงน้ำ

ขณะที่เธอดำดิ่งลงสู่ระดับความลึก ซาร่าห์รู้สึกทึ่งกับความงามของแนวปะการัง สีสันนั้นสดใสและมีชีวิตชีวา และปลาก็แหวกว่ายอยู่ในน้ำด้วยสีสันอันแพรวพราว

แต่ไฮไลท์ที่แท้จริงของการดำน้ำมาถึงเมื่อพวกเขาพบฝูงฉลาม หัวใจของ Sarah เต้นรัวขณะที่พวกมันแล่นผ่านน้ำ ดูเหมือนเกือบจะเต้นไปรอบๆ นักประดาน้ำ เธอมักจะกลัวฉลามเล็กน้อย แต่เธอก็อดไม่ได้ที่จะรู้สึกเกรงขามและเคารพเมื่อมองดูพวกมัน

ขณะที่พวกเขากลับมา ซาร่าห์ก็หยุดยิ้มไม่ได้ เธอรู้ว่าเธอเพิ่งมีประสบการณ์ที่เธอจะไม่มีวันลืม

ส่วนที่เหลือของการเดินทางสดบนเรือก็น่าทึ่งไม่แพ้กัน การดำน้ำแต่ละครั้งจะนำสิ่งมหัศจรรย์ใหม่ๆ มาให้ค้นพบ ซาร่าห์รู้ว่าเธอมักจะรักษาความทรงจำในช่วงเวลาที่เธออยู่ที่เกาะสิมิลัน และเธอแทบรอไม่ไหวที่จะกลับมาสำรวจโลกใต้น้ำให้มากขึ้น
""" 

# mytext.replace('\n',' ')

# mytext = "Hi, this is an example of converting text to audio. This is a bot speaking here, not a real human!"


audio = gTTS(text=mytext, lang="th", slow=False)
audio.save("example1.mp3")
os.system("start example1.mp3")


mytext = """ It was a hot and humid day in Phuket, and the sun was beating down on the crowded streets. But Sarah didn't mind the heat - she was too excited to be diving in the beautiful Similan Islands.

Sarah had always been fascinated by the sea, and she had been dreaming of exploring the crystal clear waters of the Similan Islands for as long as she could remember. So when she finally had the opportunity to take a live-onboard dive trip to the islands, she jumped at the chance.

The live-onboard dive boat was small and cozy, with just enough room for the six divers and the crew. Sarah quickly made friends with the other divers, who were all seasoned veterans with hundreds of dives under their belts.

As they sailed out to the Similan Islands, Sarah couldn't help but feel a sense of excitement and anticipation building inside of her. She had heard that the Similan Islands were home to some of the most beautiful coral reefs in the world, and she couldn't wait to see them for herself.

Finally, after what seemed like an eternity, they arrived at their first dive site. Sarah and the other divers donned their gear and prepared to enter the water.

As she descended into the depths, Sarah was awestruck by the beauty of the coral reefs. The colors were vibrant and alive, and the fish swam through the water in a dazzling array of hues.

But the real highlight of the dive came when they encountered a group of sharks. Sarah's heart raced as they glided through the water, seeming to almost dance around the divers. She had always been a little bit afraid of sharks, but she couldn't help but feel a sense of awe and respect as she watched them.

As they resurfaced, Sarah couldn't stop smiling. She knew that she had just had an experience that she would never forget.

The rest of the live-onboard trip was just as incredible, with each dive bringing new wonders to discover. Sarah knew that she would always treasure the memories of her time in the Similan Islands, and she couldn't wait to come back and explore more of the underwater world.
""" 



audio = gTTS(text=mytext, lang="en", slow=False)
audio.save("example2.mp3")
os.system("start example2.mp3")
