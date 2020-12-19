---
title: Varioskan LUX Plate Reader
header-includes: |
    \usepackage{fancyhdr}
    \pagestyle{fancy}
    \usepackage{lastpage}
    \usepackage{graphicx}
    \fancyhead[LO,LE]{Department of Chemistry, Tufts University}
    \fancyfoot[LO,LE]{Revised
    \date{\today}}
    \fancyfoot[RO,RE]{Morimoto}
    \cfoot{\thepage / \pageref{LastPage}}
---
## Preparation
1. Pipette your samples in an appropriate scheme on a well plate. An
   example scheme from the undergrad labs is shown below. Include blanks,
   standards, and your sample

   ![plate](images/plate.jpg){ height=360px }\

## Acquisition

2. Start the `SkanIt` software on the attached PC
3. Click `Other instrument types` and select `New session for Varioskan LUX`
4. Select `Plate Layout` from the tree on the left
5. In the `Plate template` dropdown menu, select the appropriate plate for
   analysis, most likely `Corning, U-bottom, 96-well`
6. Populate the wells in the software according to their sample type. You can
   drag the cursor to populate multiple wells
7. Select `Protocol` in the session tree and click `Absorbance`, `Fluorescence`,
   `Luminescence`, or `TRF` depending on your assay. Input the appropriate
   parameters, e.g. measurement wavelength for `Absorbance`
8. *Optional* Select `Protocol` in the session tree to change measurement order
   and delay
9. *Optional* Select `Report` to customize the output of your results
10. In the bottom left of the window, click the button with the red arrow to
    eject the plate reader tray

    ![eject](images/plate_controls.png){ height=120px }\

11. Insert the plate into the tray **with the lid off**. Leaving the lid on will
    cause a jam
12. Click the button with the green upwards arrow to insert the plate into the
    instrument
13. Click `Start` to begin the assay. Save your experiment with the appropriate
    directory and filename

## Reporting

14. Under the `Report` branch, click `Summary`. From the top right, select your
    desired reporting format to export.

For more information see the full instruction manuals at

[https://assets.thermofisher.com/TFS-Assets/LCD/manuals/Varioskan-LUX-Technical-Manual.pdf](https://assets.thermofisher.com/TFS-Assets/LCD/manuals/Varioskan-LUX-Technical-Manual.pdf)

and

[https://assets.thermofisher.com/TFS-Assets/LCD/manuals/Varioskan-LUX-User-Manual.pdf](https://assets.thermofisher.com/TFS-Assets/LCD/manuals/Varioskan-LUX-User-Manual.pdf)
