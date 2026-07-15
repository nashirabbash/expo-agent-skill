---
title: "DateTimePicker"
description: "A Jetpack Compose DateTimePicker component for selecting dates and times."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/datetimepicker.md"
scraped_at: "2026-07-15T09:00:52.789843"
---

---
title: DateTimePicker
description: A Jetpack Compose DateTimePicker component for selecting dates and times.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# DateTimePicker

A Jetpack Compose DateTimePicker component for selecting dates and times.
Android, Included in Expo Go

Expo UI DateTimePicker matches the official Jetpack Compose [Date Picker](https://developer.android.com/develop/ui/compose/components/datepickers) and [Time Picker](https://developer.android.com/develop/ui/compose/components/time-pickers) APIs and supports date, time, and combined selection.

> **Note:** The date variants render Material's calendar grid and input field, both of which scroll horizontally internally. The parent `Host` must provide a finite width on the horizontal axis, use `matchContents={{ vertical: true }}` together with `style={{ width: '100%' }}` (or any finite width). See [Match contents in Host reference](/versions/latest/sdk/ui/jetpack-compose/host.md#match-contents) for details.

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

### Date picker

```tsx
import { useState } from 'react';
import { Host, DateTimePicker } from '@expo/ui/jetpack-compose';

export default function DatePickerExample() {
  const [selectedDate, setSelectedDate] = useState(new Date());

  return (
    <Host matchContents={{ vertical: true }} style={{ width: '100%' }}>
      <DateTimePicker
        onDateSelected={date => {
          setSelectedDate(date);
        }}
        displayedComponents="date"
        initialDate={selectedDate.toISOString()}
        variant="picker"
      />
    </Host>
  );
}
```

### Time picker

```tsx
import { useState } from 'react';
import { Host, DateTimePicker } from '@expo/ui/jetpack-compose';

export default function TimePickerExample() {
  const [selectedDate, setSelectedDate] = useState(new Date());

  return (
    <Host matchContents={{ vertical: true }} style={{ width: '100%' }}>
      <DateTimePicker
        onDateSelected={date => {
          setSelectedDate(date);
        }}
        displayedComponents="hourAndMinute"
        initialDate={selectedDate.toISOString()}
        variant="picker"
      />
    </Host>
  );
}
```

### Input variant

Use `variant="input"` to display the picker as a text input field instead of the default picker UI.

```tsx
import { useState } from 'react';
import { Host, DateTimePicker } from '@expo/ui/jetpack-compose';

export default function InputVariantExample() {
  const [selectedDate, setSelectedDate] = useState(new Date());

  return (
    <Host matchContents={{ vertical: true }} style={{ width: '100%' }}>
      <DateTimePicker
        onDateSelected={date => {
          setSelectedDate(date);
        }}
        displayedComponents="date"
        initialDate={selectedDate.toISOString()}
        variant="input"
      />
    </Host>
  );
}
```

## API

```tsx
import { DateTimePicker } from '@expo/ui/jetpack-compose';
```

## Components

### `DatePickerDialog`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[DatePickerDialogProps](#datepickerdialogprops)\>

DatePickerDialogProps

### `color`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

### `confirmButtonLabel`

Supported platforms: Android.

Optional • Type: `string`

### `dismissButtonLabel`

Supported platforms: Android.

Optional • Type: `string`

### `elementColors`

Supported platforms: Android.

Optional • Type: [DatePickerElementColors](#datepickerelementcolors) & [TimePickerElementColors](#timepickerelementcolors)

### `initialDate`

Supported platforms: Android.

Optional • Literal type: `union`

Acceptable values are: `string` | `null`

### `onDateSelected`

Supported platforms: Android.

Optional • Type: (date: [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)) => void

### `onDismissRequest`

Supported platforms: Android.

Type: `() => void`

### `selectableDates`

Supported platforms: Android.

Optional • Type: { end: [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date), start: [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) }

### `showVariantToggle`

Supported platforms: Android.

Optional • Type: `boolean`

### `variant`

Supported platforms: Android.

Optional • Type: [AndroidVariant](#androidvariant)

### `DateTimePicker`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[DateTimePickerProps](#datetimepickerprops)\>

Renders an inline `DateTimePicker` component.

DateTimePickerProps

### `color`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The tint color to use on the picker elements. When `elementColors` is not provided, this color is applied to a subset of picker elements (selected day, title, headline, today border for date picker; selector, selected time segment, clock dial for time picker).

### `displayedComponents`

Supported platforms: Android.

Optional • Type: [DisplayedComponents](#displayedcomponents) • Default: `'date'`

The components that the picker should display. On Android, you can have a picker that selects just the date or just the time. `dateAndTime` is only available on iOS and will result in a date picker on Android. On iOS, you can have a picker that selects both date and time.

### `elementColors`

Supported platforms: Android.

Optional • Type: [DatePickerElementColors](#datepickerelementcolors) & [TimePickerElementColors](#timepickerelementcolors)

Fine-grained color overrides for individual picker elements. When provided, these take precedence over the `color` prop. Date picker color keys are used when `displayedComponents` is 'date' or 'dateAndTime'. Time picker color keys are used when `displayedComponents` is 'hourAndMinute'. Unset values fall back to Material 3 theme defaults.

### `initialDate`

Supported platforms: Android.

Optional • Literal type: `union`

The initial date to display on the picker.

Acceptable values are: `string` | `null`

### `is24Hour`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Determines what format the clock should be displayed in on Android.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onDateSelected`

Supported platforms: Android.

Optional • Type: (date: [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)) => void

Callback function that is called when a date is selected.

### `selectableDates`

Supported platforms: Android.

Optional • Type: { end: [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date), start: [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) }

Constrains which dates can be selected. Mirrors the native Compose `selectableDates` parameter. `start` is the earliest selectable date, `end` is the latest.

### `showVariantToggle`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Show to button to toggle between variants on Android.

### `variant`

Supported platforms: Android.

Optional • Type: [AndroidVariant](#androidvariant) • Default: `'picker'`

The variant of the picker, which determines its appearance and behavior.

### `TimePickerDialog`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[TimePickerDialogProps](#timepickerdialogprops)\>

TimePickerDialogProps

### `color`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

### `confirmButtonLabel`

Supported platforms: Android.

Optional • Type: `string`

### `dismissButtonLabel`

Supported platforms: Android.

Optional • Type: `string`

### `elementColors`

Supported platforms: Android.

Optional • Type: [DatePickerElementColors](#datepickerelementcolors) & [TimePickerElementColors](#timepickerelementcolors)

### `initialDate`

Supported platforms: Android.

Optional • Literal type: `union`

Acceptable values are: `string` | `null`

### `is24Hour`

Supported platforms: Android.

Optional • Type: `boolean`

### `onDateSelected`

Supported platforms: Android.

Optional • Type: (date: [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)) => void

### `onDismissRequest`

Supported platforms: Android.

Type: `() => void`

## Types

### `AndroidVariant`

Supported platforms: Android.

Literal Type: `string`

Acceptable values are: `'picker'` | `'input'`

### `DatePickerElementColors`

Supported platforms: Android.

Color overrides for the Material 3 DatePicker component. All properties are optional — unset values use Material 3 theme defaults.

| Property | Type | Description |
| --- | --- | --- |
| containerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The background color of the date picker. |
| currentYearContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for the current year content. |
| dayContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for day content (number text). |
| dayInSelectionRangeContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The container color for days within a date range selection. |
| dayInSelectionRangeContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The content color for days within a date range selection. |
| disabledDayContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for disabled day content. |
| disabledSelectedDayContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for a disabled selected day container. |
| disabledSelectedDayContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for a disabled selected day content. |
| disabledSelectedYearContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for a disabled selected year container. |
| disabledSelectedYearContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for a disabled selected year content. |
| disabledYearContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for disabled year item content. |
| dividerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for divider lines. |
| headlineContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for the date picker's headline. |
| navigationContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for navigation arrows and year selection menu button. |
| selectedDayContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for the selected day container/background circle. |
| selectedDayContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for selected day content. |
| selectedYearContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for the selected year container/background. |
| selectedYearContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for the selected year content. |
| subheadContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for the month and year subhead labels. |
| titleContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for the date picker's title. |
| todayContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for today's date text. |
| todayDateBorderColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for today's date border. |
| weekdayContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for the weekday letters (Mon, Tue, etc.). |
| yearContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color used for year item content. |

### `DisplayedComponents`

Supported platforms: Android.

Literal Type: `string`

Acceptable values are: `'date'` | `'hourAndMinute'` | `'dateAndTime'`

### `TimePickerElementColors`

Supported platforms: Android.

Color overrides for the Material 3 TimePicker component. All properties are optional — unset values use Material 3 theme defaults.

| Property | Type | Description |
| --- | --- | --- |
| clockDialColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The background color of the clock dial. |
| clockDialSelectedContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color of clock dial numbers when selected or overlapping the selector. |
| clockDialUnselectedContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color of clock dial numbers when unselected. |
| containerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The container/background color of the time picker. |
| periodSelectorBorderColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The border color of the AM/PM period selector. |
| periodSelectorSelectedContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The background color of the selected AM/PM period. |
| periodSelectorSelectedContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The text color of the selected AM/PM period. |
| periodSelectorUnselectedContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The background color of the unselected AM/PM period. |
| periodSelectorUnselectedContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The text color of the unselected AM/PM period. |
| selectorColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The color of the clock dial selector (hand). |
| timeSelectorSelectedContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The background color of the selected hour/minute segment. |
| timeSelectorSelectedContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The text color of the selected hour/minute segment. |
| timeSelectorUnselectedContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The background color of the unselected hour/minute segment. |
| timeSelectorUnselectedContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | The text color of the unselected hour/minute segment. |
