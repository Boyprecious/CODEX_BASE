import  CEASER
import  qrcode as coder

CEASER.type_effect("This is codexbase security world!", 0.1)
print("\n")
inputt = input(CEASER.type_effect("enter information: ", 0.1))

text_result = CEASER.ceaser(inputt)
print(text_result)
CEASER.type_effect("Generating in a minute!", 0.1)

image = coder.make(text_result)
image.save("Security_code.png")
image.show("Security_code.png")

CEASER.type_effect("Thank you for using me", 0.3)

