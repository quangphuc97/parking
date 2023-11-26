<h1>Calculate the price for parking</h1>
<h2>Input:</h2>
<br>-Arrival time (format yyyy-mm-dd H:M)
<br>-Leave time (format yyyy-mm-dd H:M)
<br>-Frequent parking (5 character)
<h2>Valid frequent parking will get discount:</h2>
<br>-50% for parking time: 17:00 - Midnight, Midnight - 08:00.
<br>-10% for other parking time

<table>
<thead>
  <tr>
    <th rowspan="3">Day of week</th>
    <th colspan="6">Arrial Time</th>
  </tr>
  <tr>
    <th colspan="2">From 08:00 - 16:59</th>
    <th colspan="2">From 17:00 - Midnight</th>
    <th colspan="2">Midnight - 07:59</th>
  </tr>
  <tr>
    <th>Max stay in hours</th>
    <th>Price per hour</th>
    <th>Max stay in hours</th>
    <th>Price per hour</th>
    <th>Max stay in hours</th>
    <th>Price (one time)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Sunday</td>
    <td>8</td>
    <td>2.0</td>
    <td>Up to midnight</td>
    <td>5.0</td>
    <td>None</td>
    <td>20.0</td>
  </tr>
  <tr>
    <td>Monday</td>
    <td>2</td>
    <td>10.0</td>
    <td>Up to midnight</td>
    <td>5.0</td>
    <td>None</td>
    <td>20.0</td>
  </tr>
  <tr>
    <td>Tuesday</td>
    <td>2</td>
    <td>10.0</td>
    <td>Up to midnight</td>
    <td>5.0</td>
    <td>None</td>
    <td>20.0</td>
  </tr>
  <tr>
    <td>Wednesday</td>
    <td>2</td>
    <td>10.0</td>
    <td>Up to midnight</td>
    <td>5.0</td>
    <td>None</td>
    <td>20.0</td>
  </tr>
  <tr>
    <td>Thursday</td>
    <td>2</td>
    <td>10.0</td>
    <td>Up to midnight</td>
    <td>5.0</td>
    <td>None</td>
    <td>20.0</td>
  </tr>
  <tr>
    <td>Friday</td>
    <td>2</td>
    <td>10.0</td>
    <td>Up to midnight</td>
    <td>5.0</td>
    <td>None</td>
    <td>20.0</td>
  </tr>
  <tr>
    <td>Saturday</td>
    <td>4</td>
    <td>3.0</td>
    <td>Up to midnight</td>
    <td>5.0</td>
    <td>None</td>
    <td>20.0</td>
  </tr>
</tbody>
</table>
