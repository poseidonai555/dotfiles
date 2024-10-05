# Digital certificates and signatures

## What is a digital signature

- It uses a mathematical function and a public/private key method to create a unique signature which is attached to the message before being sent

## What is a digital certificate

- This ensures an encrypted message is from a trusted source, the source will have a certification and a certification authority

## What is a certification authority

- An organization that provides digital certificates

## How is a private key signature created

- A hash function is applied to a document

- The digest is encrypted using the user's private key (making it clear that the user is the owner of the message)

- The encrypted digest is what we call the digital signature

## How is the private key signature used

- After a digital signature has been created, it is attached to the original plain text message

- The entire thing is encrypted using the user's copy of the public key

- The message can then be decrypted by others by using their own private keys

- The digital signature is then decrypted using the senders copy of the public key which the recipient holds

- The message digest is then regenerated

- The regenerated digest and the original digest are compared'

- If they are not identical, it is clear that someone has intercepted or altered the message