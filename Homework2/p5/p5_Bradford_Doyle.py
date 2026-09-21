from datetime import datetime
import sys

def main() -> None:
    """Read observations, display results, and write station statistics."""
    if len(sys.argv) != 3:
        print(
            "Usage: python p5_Bradford_Doyle.py "
            "input_observations.txt output_statistics.txt"

        )
        return
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        observations, errors = read_observations(input_filename)

        for line_number, message in errors:
            print(f"Line {line_number}: {message}")
   
        statistics =station_statistics(observations)
        outliers = station_outliers(observations)

        print("station statistics:")
        for station in sorted(statistics):
            print(station, statistics[station])

        print("Station outliers:")
        for station in sorted(outliers):
            print(station, outliers[station])

        write_statistics(output_filename, statistics)
        print(f"Statistics written to {output_filename}") 
    except FileNotFoundError as error:
        print(f"File or directory not found: {error.filename}")

    except OSError as error:
        print(f"Unable to read or write a file: {error}")


##reads the fileand builds observations dict
def read_observations(filename: str) -> tuple:
    """Read observation file; return dict of station data and list or errors."""
    observations = {}
    errors = []
    seen = set()

    with open(filename, "r", encoding="utf-8") as infile:
        for line_number, line in enumerate(infile, start=1):
            fields = line.strip().split(",")

            if len(fields) != 3:
                errors.append((line_number, "Expected 3 comma-separated fields"))
                continue

            station, date_text, tempt_text = [
                field.strip() for field in fields
            ]

            if not station:
                errors.append((line_number, "Missing station"))
                continue

            try:
                date = datetime.strptime(
                    date_text, "%I:%M:%S %p %m/%d/%Y"
                )
            except ValueError:
                errors.append((line_number, "Invalid date or time"))
                continue
            try:
                temperature = float(tempt_text
                )
            except ValueError:
                errors.append((line_number, "Temperature must be a number"))
                continue

            if not -100 <= temperature <= 150:
                errors.append((line_number, "Temperature must be between -100 and 150"))
                continue

            key = (station, date_text)
            if key in seen: 
                errors.append((line_number, "Duplicate station and date"))
                continue
            seen.add(key)
            
            if station not in observations:
                observations[station] = []
            observations[station].append((date_text, temperature))

    for station in observations:
##sorts each of them by date seing datetime
      observations[station].sort(
          key=lambda item: datetime.strptime(item[0], "%I:%M:%S %p %m/%d/%Y")) 
    return observations, errors

##gets the most recent emp above mean
def station_statistics(observations: dict[str, list[tuple[datetime, float]]]) -> dict[str, tuple[float, float, float]]:
    """Return (minimum, maximum, mean) temperatures for each nonempty station."""
    statistics = {}

    for station , readings in observations.items():
        if not readings:
            continue

        temperatures = [temperature for date, temperature in readings]
        minimum = min(temperatures)
        maximum = max(temperatures)
        mean = sum(temperatures) / len(temperatures)

        statistics[station] = (minimum, maximum, mean)
    return statistics

##
def station_outliers(observations: dict[str, list[tuple[datetime, float]]]) -> dict[str, tuple[str, float, float]]:
    """Return stations whose latest temperature is strictly above their mean."""
    statistics = station_statistics(observations)

    return {
        station: (
            latest_date, latest_temperature, statistics[station][2]
        )
        for station, readings, in observations.items()
        if readings
        
        for latest_date, latest_temperature in [readings[-1]]
        if latest_temperature > statistics[station][2]
    }
##Wrties statistics from a-z and one decimal
def write_statistics(filename: str, statistics: dict[str, tuple[float, float, float]]) -> None:
    """Write stations alphabetically with temperatures to one decimal place."""
    outfile = open(filename, "w", encoding="utf-8")

    try:
        for station in sorted(statistics):
            minimum, maximum, mean = statistics[station]
            outfile.write(f"{station},{minimum:.1f},{maximum:.1f},{mean:.1f}\n")
    finally:
        outfile.close()
    



if __name__ == "__main__":
    main()
