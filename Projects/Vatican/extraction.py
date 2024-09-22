import pythonbible as bible
import csv
import json

verse_data = []

# Define a list of references
references = [
    bible.NormalizedReference(bible.Book.GENESIS, 1, 1, 50, 26),
    bible.NormalizedReference(bible.Book.EXODUS, 1, 1, 40, 38),
    bible.NormalizedReference(bible.Book.LEVITICUS, 1, 1, 27, 34),
    bible.NormalizedReference(bible.Book.NUMBERS, 1, 1, 36, 13),
    bible.NormalizedReference(bible.Book.DEUTERONOMY, 1, 1, 34, 12),
    bible.NormalizedReference(bible.Book.JOSHUA, 1, 1, 24, 33),
    bible.NormalizedReference(bible.Book.JUDGES, 1, 1, 21, 25),
    bible.NormalizedReference(bible.Book.RUTH, 1, 1, 4, 22),
    bible.NormalizedReference(bible.Book.SAMUEL_1, 1, 1, 31, 13),
    bible.NormalizedReference(bible.Book.SAMUEL_2, 1, 1, 24, 25),
    bible.NormalizedReference(bible.Book.KINGS_1, 1, 1, 22, 53),
    bible.NormalizedReference(bible.Book.KINGS_2, 1, 1, 25, 30),
    bible.NormalizedReference(bible.Book.CHRONICLES_1, 1, 1, 29, 30),
    bible.NormalizedReference(bible.Book.CHRONICLES_2, 1, 1, 36, 23),
    bible.NormalizedReference(bible.Book.EZRA, 1, 1, 10, 43),
    bible.NormalizedReference(bible.Book.NEHEMIAH, 1, 1, 13, 30),
    bible.NormalizedReference(bible.Book.ESTHER, 1, 1, 10, 3),
    bible.NormalizedReference(bible.Book.JOB, 1, 1, 42, 17),
    bible.NormalizedReference(bible.Book.PSALMS, 1, 1, 150, 6),
    bible.NormalizedReference(bible.Book.PROVERBS, 1, 1, 31, 31),
    bible.NormalizedReference(bible.Book.ECCLESIASTES, 1, 1, 12, 14),
    bible.NormalizedReference(bible.Book.SONG_OF_SONGS, 1, 1, 8, 14),
    bible.NormalizedReference(bible.Book.ISAIAH, 1, 1, 66, 24),
    bible.NormalizedReference(bible.Book.JEREMIAH, 1, 1, 52, 34),
    bible.NormalizedReference(bible.Book.LAMENTATIONS, 1, 1, 5, 22),
    bible.NormalizedReference(bible.Book.EZEKIEL, 1, 1, 48, 35),
    bible.NormalizedReference(bible.Book.DANIEL, 1, 1, 12, 13),
    bible.NormalizedReference(bible.Book.HOSEA, 1, 1, 14, 9),
    bible.NormalizedReference(bible.Book.JOEL, 1, 1, 3, 21),
    bible.NormalizedReference(bible.Book.AMOS, 1, 1, 9, 15),
    bible.NormalizedReference(bible.Book.OBADIAH, 1, 1, 1, 21),
    bible.NormalizedReference(bible.Book.JONAH, 1, 1, 4, 11),
    bible.NormalizedReference(bible.Book.MICAH, 1, 1, 7, 20),
    bible.NormalizedReference(bible.Book.NAHUM, 1, 1, 3, 19),
    bible.NormalizedReference(bible.Book.HABAKKUK, 1, 1, 3, 19),
    bible.NormalizedReference(bible.Book.ZEPHANIAH, 1, 1, 3, 20),
    bible.NormalizedReference(bible.Book.HAGGAI, 1, 1, 2, 23),
    bible.NormalizedReference(bible.Book.MALACHI, 1, 1, 4, 6),
    bible.NormalizedReference(bible.Book.MATTHEW, 1, 1, 28, 20),
    bible.NormalizedReference(bible.Book.MARK, 1, 1, 16, 20),
    bible.NormalizedReference(bible.Book.LUKE, 1, 1, 24, 53),
    bible.NormalizedReference(bible.Book.JOHN, 1, 1, 21, 25),
    bible.NormalizedReference(bible.Book.ACTS, 1, 1, 28, 31),
    bible.NormalizedReference(bible.Book.ROMANS, 1, 1, 16, 27),
    bible.NormalizedReference(bible.Book.CORINTHIANS_1, 1, 1, 16, 24),
    bible.NormalizedReference(bible.Book.CORINTHIANS_2, 1, 1, 13, 14),
    bible.NormalizedReference(bible.Book.GALATIANS, 1, 1, 6, 18),
    bible.NormalizedReference(bible.Book.EPHESIANS, 1, 1, 6, 24),
    bible.NormalizedReference(bible.Book.PHILIPPIANS, 1, 1, 4, 23),
    bible.NormalizedReference(bible.Book.COLOSSIANS, 1, 1, 4, 18),
    bible.NormalizedReference(bible.Book.THESSALONIANS_1, 1, 1, 5, 28),
    bible.NormalizedReference(bible.Book.THESSALONIANS_2, 1, 1, 3, 18),
    bible.NormalizedReference(bible.Book.TIMOTHY_1, 1, 1, 6, 21),
    bible.NormalizedReference(bible.Book.TIMOTHY_2, 1, 1, 4, 22),
    bible.NormalizedReference(bible.Book.TITUS, 1, 1, 3, 15),
    bible.NormalizedReference(bible.Book.PHILEMON, 1, 1, 1, 25),
    bible.NormalizedReference(bible.Book.HEBREWS, 1, 1, 13, 25),
    bible.NormalizedReference(bible.Book.JAMES, 1, 1, 5, 20),
    bible.NormalizedReference(bible.Book.PETER_1, 1, 1, 5, 14),
    bible.NormalizedReference(bible.Book.PETER_2, 1, 1, 3, 18),
    bible.NormalizedReference(bible.Book.JOHN_1, 1, 1, 5, 21),
    bible.NormalizedReference(bible.Book.JOHN_2, 1, 1, 1, 13),
    bible.NormalizedReference(bible.Book.JOHN_3, 1, 1, 1, 14),
    bible.NormalizedReference(bible.Book.JUDE, 1, 1, 1, 25),
    bible.NormalizedReference(bible.Book.REVELATION, 1, 1, 22, 21),
]

# Convert the list of references to verse IDs
verse_ids = bible.convert_references_to_verse_ids(references)

# Convert verse IDs to references
references_from_ids = bible.convert_verse_ids_to_references(verse_ids)

# Function to format NormalizedReference to string
def format_reference(ref):
    book_name = ref.book.name
    start_chapter = ref.start_chapter
    start_verse = ref.start_verse
    end_chapter = ref.end_chapter if ref.end_chapter else start_chapter
    end_verse = ref.end_verse if ref.end_verse else start_verse
    
    if start_chapter == end_chapter and start_verse == end_verse:
        ref_str = f"{book_name} {start_chapter}:{start_verse}"
    else:
        ref_str = f"{book_name} {start_chapter}:{start_verse}-{end_chapter}:{end_verse}"
    
    return ref_str

# Main loop to show random verse, and ask for reference. If incorrect show the reference as a hint. When correct show Job 38:11 with the reference, and continue loop.

# Print Verse Reference and Verse Text, and collect data
for verse_id in verse_ids:
    verse_text = bible.get_verse_text(verse_id)
    ref = bible.convert_verse_ids_to_references([verse_id])[0]
    ref_str = format_reference(ref)

    # Append data to the list
    verse_data.append({"reference": ref_str, "text": verse_text})

# Save to CSV
csv_filename = 'verses.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['reference', 'text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for data in verse_data:
        writer.writerow(data)

print(f"Data has been saved to {csv_filename}")

# Save to JSON
json_filename = 'verses.json'
with open(json_filename, 'w', encoding='utf-8') as jsonfile:
    json.dump(verse_data, jsonfile, ensure_ascii=False, indent=4)

print(f"Data has been saved to {json_filename}")
