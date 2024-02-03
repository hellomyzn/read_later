import csv
import datetime
import sys

def get_now_jst():
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    d = now.strftime('%Y/%m/%d %H:%M:%S')
    return d

csv_file_path = "./read_later.csv"
def write_header():
    with open(csv_file_path, encoding="utf-8", mode="w") as f:
        writer = csv.DictWriter(f, fieldnames = HEADER)
        writer.writeheader()
        print(f"write header. header: {HEADER}")


KEY_ID = "id"
KEY_TITLE = "title"
KEY_URL = "url"
KEY_CREATE_AT = "create_at"

HEADER = [KEY_ID, KEY_TITLE, KEY_URL, KEY_CREATE_AT]

# get all onetab links
onetab_file_path = "./onetab.txt"
with open(onetab_file_path, encoding="utf-8") as f:
    texts = f.readlines()
texts.reverse()

# get all read_laters from csv
csv_file_path = "./read_later.csv"
with open(csv_file_path, encoding="utf-8", mode="r") as f:
    reader = csv.DictReader(f)

    # check header
    header = reader.fieldnames
    if header is None:
        print(f"header is None. header: {header}")
        write_header()
    elif header != HEADER:
        print(f"header is not. header: {header}, expected header: {HEADER}")
        sys.exit(1)
    all_read_laters = [row for row in reader]

# prepare
read_laters = []
id_ = 1
if all_read_laters:
    id_ = int(all_read_laters[-1][KEY_ID]) + 1
create_at = get_now_jst()

for text in texts:
    # there some "\n" values in texts from onetab and avoid them
    if text == "\n": 
        continue

    splitted_text = text.split("|")
    url = splitted_text[0].replace("\n","")
    title = "".join(splitted_text[1:]).replace("\n", "").lstrip()

    # sometimes title is error_title which is not legit
    error_texts = ["400 Request Header Or Cookie Too Large",
     "The page you were looking for doesn't exist",
     "404 Not Found - Qiita"]
    if any(error_text in title for error_text in error_texts):
        print(f"has error texts in title. title: {title}, url: {url}")
        sys.exit(1)

    # skip if duplicated data with onetab
    if any(url == rl["url"] for rl in read_laters):
        continue

    # skip if url exists in the csv
    if any(url == arl["url"] for arl in all_read_laters):
        continue

    read_later = {}
    values = [id_, title, url, create_at]
    for key, val in zip(HEADER, values):
        read_later.update({key: val})
    read_laters.append(read_later)
    id_ += 1


if not read_laters:
    print("no new read later")
    sys.exit(1)

# csv
with open(csv_file_path, encoding="utf-8", mode="a") as f:
    writer = csv.DictWriter(f, fieldnames = HEADER)
    writer.writerows(read_laters)



# TODO: reads csvを用意して、google spread sheetからデータを取得し、ローカルcsv に同期して、githubで管理する
