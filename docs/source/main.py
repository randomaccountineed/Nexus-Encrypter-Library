import nexusencrypter

### Key Example

key="齊匚.說(≤蹄片q@刻≫木₴生h🂺{宗拇陽p卞/F>÷讓御ﾌ無≪…X🃚ㄒ至Nt父冊C◩方WɎ]₥K甲乇×k勹水ᐯⱧ5丂雜內lgPҜn≥逍徐Ⱡ◎間Ɽ廾符ZSɄ❒🟥y,馬達$寇🃁~z□乍🃖養山尸師🟩V🂭篋ㄥfɆ知MᎶ胠地應9฿◫"

### Text Example For Encryption

text="Hello World!"

### Text Example For Decryption

text2="🃚生ppF…M…F讓p₴"

### Encrypt An Message Using Encrypt Function. Get Key From: .key File, 
### Directly From String Or Random (idk where this could be usefull to)!

result = nexusencrypter.encrypt(text=text, key=key)

### Decrypt An Message Using Decrypt Function. Get Key From: .key File, 
### Directly From String (dont try using random key)!

result2 = nexusencrypter.decrypt(text=text2, key=key)

### Create A Custom Key And Export to File Using Create Function Leave Blank For Random
### Key. Insert Key For  Set Key

nexusencrypter.create(name="keyname" ,key="")

### You Can Save The Result Of An Decryption/ Encryption In A Variable And Then Use It 
## However You Want!

print(result)
                                 
print(result2)