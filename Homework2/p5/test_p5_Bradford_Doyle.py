import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from p5_Bradford_Doyle import (
    read_observations,
    station_statistics,
    write_statistics,
)

class TestStationFunctions(unittest.TestCase):
    def setUp(self):
        """Create temporary input files for each test."""
        self.temp_directory = TemporaryDirectory()
        self.folder = Path(self.temp_directory.name)

        self.valid_file = self.folder / "observations.txt"
        self.valid_file.write_text(
            "Beta,09:00:00 AM 04/21/2026,30\n"
            "Alpha,09:00:00 AM 04/20/2026,-10\n"
            "Beta,09:00:00 AM 04/20/2026,10\n"
            "Alpha,09:00:00 AM 04/21/2026,20\n",
            encoding="utf-8",
        )

        self.duplicate_file = self.folder / "duplicates.txt"
        self.duplicate_file.write_text(
            "Alpha,09:00:00 AM 04/20/2026,10\n"
            "Alpha,09:00:00 AM 04/20/2026,20\n",
            encoding="utf-8",
        )

        self.invalid_file = self.folder / "invalid.txt"
        self.invalid_file.write_text(
            "Alpha,09:00:00 AM 04/20/2026,151\n"
            "Beta,09:00:00 AM 04/20/2026,-101\n",
            encoding="utf-8",
        )

        self.output_file = self.folder / "statistics.txt"

    def tearDown(self):
        """Remove the temporary directory and its files."""
        self.temp_directory.cleanup()

    def test_multiple_stations_and_date_order(self):
        observations, errors = read_observations(str(self.valid_file))

        self.assertEqual(errors, [])
        self.assertEqual(set(observations), {"Alpha", "Beta"})
        self.assertEqual(
            observations["Beta"],
            [
                ("09:00:00 AM 04/20/2026", 10.0),
                ("09:00:00 AM 04/21/2026", 30.0),
            ],
        )
        self.assertEqual(len(observations["Alpha"]), 2)

    def test_valid_negative_temperature(self):
        observations, errors = read_observations(str(self.valid_file))

        self.assertEqual(errors, [])
        self.assertEqual(observations["Alpha"][0][1], -10.0)

    def test_duplicate_station_and_date(self):
        observations, errors = read_observations(str(self.duplicate_file))

        self.assertEqual(observations["Alpha"], [("09:00:00 AM 04/20/2026", 10.0)],)

        self.assertEqual(errors, [(2, "Duplicate station and date")],)

    def test_temperature_outside_range(self):
        observations, errors = read_observations(str(self.invalid_file))

        self.assertEqual(observations, {})
        self.assertEqual(errors,[(1, "Temperature must be between -100 and 150"),(2, "Temperature must be between -100 and 150"),],)    

    def test_minimum_maximum_and_mean(self):
            observations = {
                "Alpha": [
                    ("09:00:00 AM 04/20/2026", -10.0),
                    ("09:00:00 AM 04/21/2026", 20.0),
                ],
                "Beta": [
                    ("09:00:00 AM 04/20/2026", 10.0),
                    ("09:00:00 AM 04/21/2026", 30.0),
                ],
            }

            statistics = station_statistics(observations)

            self.assertEqual(statistics["Alpha"], (-10.0, 20.0, 5.0))


    def test_write_statistics_order_and_format(self):
        statistics = {
            "Beta": (10.0, 30.0, 20.0),
            "Alpha": (-10.25, 20.75, 5.25), 
        }

        write_statistics(str(self.output_file), statistics)
        contents= self.output_file.read_text(encoding="utf-8")
        self.assertEqual(
                contents,
                "Alpha,-10.2,20.8,5.2\n"
                "Beta,10.0,30.0,20.0\n",
        )

    def test_missing_file(self):   
        missing_file = self.folder /"does_not_exist.txt"

        with self.assertRaises(FileNotFoundError):
            read_observations(str(missing_file))

if __name__ == '__main__':
    unittest.main()