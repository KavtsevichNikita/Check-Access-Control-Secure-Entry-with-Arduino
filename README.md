# ChipCheck Access Control

## Project Description

1. Overview and Task Analysis
  The "ChipCheck Access Control" project aims to create an access control system using Arduino and electronic cards or chips for user identification. Its goal is to provide secure and convenient access to specific areas or resources. The project involves creating an integrated system that allows identity verification using electronic cards or chips and subsequent access control based on this identification.

2. Justification of Chosen Technologies
   Arduino was chosen as the platform for this project due to its ease of use, flexibility, and availability for most users. Additionally, it can integrate with various peripheral devices, allowing for easy expansion of the system's functionality.

3. Simple Service Diagram and Connections
  DIAGRAM

4. Contribution Breakdown of Team Members to Solution Functionality
   - Maksym Tiutiunnyk (Software Engineer): Implemented the main logic of the system in Arduino language, including reading and processing data from electronic cards and controlling access.
   - Mikita Kautsevich (Software Engineer): Implemented the main logic of the system in Arduino language, including reading and processing data from electronic cards and controlling access.
   - Sofiia Pravytska (Hardware Engineer): Designed and built the physical module with a card reader and other peripheral devices. Also responsible for integrating hardware with Arduino.
   - Yaroslav Sabadash (Hardware Engineer): Designed and built the physical module with a card reader and other peripheral devices. Also responsible for integrating hardware with Arduino.

## Installation

1. Download or clone the repository to your computer.
2. Connect Arduino to your computer using a USB cable.
3. Open the `ChipCheck_Access_Control.ino` file in the Arduino IDE.
4. Upload the sketch to your Arduino.

## Getting Started

1. Connect the card reader to Arduino according to the wiring diagram.
2. Connect electronic cards or chips that will be used for user identification.
3. Upload the list of authorized users to Arduino (this can be done through Arduino code or an external interface).
4. Power on Arduino.

## Inputs

- Card reader for electronic cards or chips.
- Arduino ports for connecting the reader and other devices.

## Outputs

- Access control mechanism (e.g., electromagnetic lock or relay to control the lock).
- Status indicators (e.g., LEDs) to indicate access status (allowed/denied).

## Example Usage

1. A user presents their electronic card to the card reader.
2. Arduino analyzes the information from the card and compares it with the database of authorized users.
3. Upon a match, Arduino grants access and controls the door-opening mechanism.
4. The user enters the premises.
