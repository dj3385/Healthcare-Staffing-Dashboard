Developing a Healthcare Staffing Dashboard for Recruiter Performance Monitoring

Healthcare staffing agencies play a crucial role in connecting healthcare professionals with facilities in need of their expertise. To streamline and improve the operational efficiency of recruiters, this project focuses on building a Python-based dashboard to monitor recruiter performance effectively.

## Project Overview

This project leverages Python and libraries such as Pandas and Matplotlib to develop a recruiter performance dashboard for the healthcare staffing industry. The dashboard provides actionable insights into key performance metrics (KPIs) like Submissions, Client Submissions, Interviews, Hires, and more.

### Features
- **Data Cleaning**: Handles missing values, renames columns for clarity, and processes raw data into a clean format.
- **KPIs Display**: Provides visual insights into essential metrics like Submissions, Client Submissions, and Hires.
- **Visualization**: Generates graphical outputs for better understanding and decision-making.
- **Automation**: Simplifies performance tracking for healthcare staffing recruiters.


### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/healthcare-staffing-dashboard.git
   ```
2. Navigate to the project directory:
   ```bash
   cd healthcare-staffing-dashboard
   ```
3. Place your Excel file (`data.xlsx`) in the project directory.
4. Run the Python script:
   ```bash
   python dashboard.py
   ```
5. The dashboard will process the data and generate visual insights.

## Project Structure

- `dashboard.py`: The main script that processes data and generates the dashboard.
- `data.xlsx`: Input file containing recruiter performance data.
- `README.md`: Detailed documentation of the project.

## Key Performance Indicators (KPIs)

1. **Submissions**: Total profiles submitted by recruiters.
2. **Client Submissions**: Profiles shared with clients.
3. **Interviews**: Interviews scheduled with end clients.
4. **Hires**: Successful placements.

## Results

The dashboard provides the following insights:

- Total Submissions: 214
- Key Observations: Recruiter performance varies, with certain recruiters significantly outperforming others.
- Graphical Representations: Pie charts, bar graphs, and line plots visually depict recruiter contributions.

### Example Output

- **Textual Insights**:
  - Recruiter `Sumit Singh` has the highest number of submissions (47).
  - Recruiter `Nehal Gadhvi` has the highest number of hires (3).

- **Graphs**:
  - Submissions by Recruiter: Displays a bar graph of submissions made by each recruiter.
  - Hires vs. Submissions: Shows a line graph of the relationship between submissions and hires.

## Future Enhancements

- **Real-time Data Updates**: Integrate APIs to fetch live data.
- **Machine Learning**: Predict recruiter performance based on historical data.
- **Web Interface**: Build a frontend for better accessibility and interaction.

## References

1. Pandas Documentation: [https://pandas.pydata.org/](https://pandas.pydata.org/)
2. Matplotlib Documentation: [https://matplotlib.org/](https://matplotlib.org/)
3. OpenPyXL Documentation: [https://openpyxl.readthedocs.io/](https://openpyxl.readthedocs.io/)

---

Feel free to fork this project, submit pull requests, or report issues to contribute to its development.
