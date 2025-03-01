def parse_csv_line(file, delimiter=';'):
    fields = []
    current_field = ''
    in_quotes = False
    
    while True:
        char = file.read(1)
        if not char:
            if current_field or fields:
                fields.append(current_field.strip())
                return fields
            return None

        if char == '"':
            in_quotes = not in_quotes
        elif char == '\n' and not in_quotes:
            fields.append(current_field.strip())
            return fields
        elif char == delimiter and not in_quotes:
            fields.append(current_field.strip())
            current_field = ''
        else:
            current_field += char

def process_music_dataset(file_path):
    composers = set()
    period_counts = {}
    period_titles = {}
    
    with open(file_path, 'r', encoding='utf-8') as file:        
        header = file.readline()
        while True:
            data = parse_csv_line(file)
            if data is None:
                break
            
            title = data[0]
            period = data[3]
            artist = data[4]
            
            composers.add(artist)
            
            if period in period_counts:
                period_counts[period] += 1
            else:
                period_counts[period] = 1
                
            if period not in period_titles:
                period_titles[period] = []
            period_titles[period].append(title)
            
        sorted_composers = sorted(composers)
        
        for period in period_titles:
            period_titles[period].sort()
            
        return sorted_composers, period_counts, period_titles

file_path = 'obras.csv'  
sorted_composers, period_counts, period_titles = process_music_dataset(file_path)

with open("compositores.txt", "w", encoding="utf-8") as f:
    for composer in sorted_composers:
        f.write(composer + "\n")

with open("distribuicao_periodos.txt", "w", encoding="utf-8") as f:
    for period, count in period_counts.items():
        f.write(f"{period}: {count}\n")

with open("obras_por_periodo.txt", "w", encoding="utf-8") as f:
    for period, titles in period_titles.items():
        f.write(f"{period}:\n")
        for title in titles:
            f.write(f"  {title}\n")