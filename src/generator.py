import random
from faker import Faker

fake = Faker()

BANK_DP = {
    "KUMARI BANK": "13015200",
    "NABIL BANK": "13010100",
    "NIC ASIA BANK": "13011400",
    "GLOBAL IME BANK": "13011700",
    "PRABHU BANK": "13011800"
}

districts = [
    "BARA","KATHMANDU","LALITPUR",
    "CHITWAN","POKHARA","BHAKTAPUR",
    "BIRATNAGAR","DHARAN"
]


def generate_boid(dp):
    client = str(random.randint(1,99999999)).zfill(8)
    return dp + client


def generate_citizenship():
    district = random.choice(districts)
    part1 = random.randint(100000,999999)
    part2 = random.randint(10000,99999)
    year = random.randint(2000,2022)

    return f"{district}-{part1}/{part2}-{year}"


def generate_record():

    bank = random.choice(list(BANK_DP.keys()))
    dp = BANK_DP[bank]

    return {

        "BOID": generate_boid(dp),

        "Name": fake.name().upper(),

        "Account Status": random.choice(["ACTIVE","DORMANT"]),

        "BO Sub Status": "INDIVIDUAL-RESIDENT",

        "Confirmation Wavied": random.choice(["Yes","No"]),

        "Gender": random.choice(["M","F"]),

        "Date Of Birth": fake.date_of_birth().strftime("%Y-%m-%d"),

        "Citizenship Number": generate_citizenship(),

        "PAN Number": random.choice([
            "N/A",
            str(random.randint(100000000,999999999))
        ]),

        "Father's/Mother's Name": fake.name().upper(),

        "Spouse/GrandFather's Name": fake.name().upper(),

        "Account Open Date": fake.date_between(
            start_date="-5y",
            end_date="today"
        ).strftime("%Y-%m-%d"),

        "Contact Number": "98"+str(random.randint(10000000,99999999)),

        "Email": random.choice([
            "N/A",
            fake.email()
        ]),

        "Address": f"{random.choice(districts)}, NEPAL",

        "Bank Name": bank,

        "Account Number": str(random.randint(1000000000,999999999999))
    }