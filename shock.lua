-- luamc can do cool things, but i'm using it to get the player's health lmao

local health = player.getHealth()
local lastknownhealth = player.getHealth()
local url = "https://api.particle.io/v1/devices/.../shock" -- This is if i want to be lazy
local auth = "..."
local function shock(amount)
    print("took "..amount.." damage")
    os.execute("curl \""..url.."\" -H \"Authorization: Bearer "..auth.."\" -H \"Content-Type: application/x-www-form-urlencoded; charset=UTF-8\"  --data \"arg="..damageTaken.."\"")
end

print("Script running")

while true do
    health = player.getHealth()
    if health < lastknownhealth then
        shock(lastknownhealth - health)
        lastknownhealth = health
    end
    if health > lastknownhealth then
        print("Healed ".. health - lastknownhealth)
        lastknownhealth = health
    end
end
