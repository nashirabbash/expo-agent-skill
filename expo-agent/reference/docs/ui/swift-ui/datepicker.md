---
title: "DatePicker"
description: "A SwiftUI DatePicker component for selecting dates and times."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/datepicker.md"
scraped_at: "2026-07-15T08:59:20.457395"
---

---
title: DatePicker
description: A SwiftUI DatePicker component for selecting dates and times.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# DatePicker

A SwiftUI DatePicker component for selecting dates and times.
iOS, Included in Expo Go

Expo UI DatePicker matches the official SwiftUI [DatePicker API](https://developer.apple.com/documentation/swiftui/datepicker) and supports styling via the [`datePickerStyle`](/versions/latest/sdk/ui/swift-ui/modifiers.md#datepickerstylestyle) modifier.

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

## Date picker

```tsx
import { useState } from 'react';
import { Host, DatePicker } from '@expo/ui/swift-ui';

export default function DatePickerExample() {
  const [selectedDate, setSelectedDate] = useState(new Date());

  return (
    <Host matchContents>
      <DatePicker
        title="Select a date"
        selection={selectedDate}
        displayedComponents={['date']}
        onDateChange={date => {
          setSelectedDate(date);
        }}
      />
    </Host>
  );
}
```

## Time picker

```tsx
import { useState } from 'react';
import { Host, DatePicker } from '@expo/ui/swift-ui';

export default function TimePickerExample() {
  const [selectedDate, setSelectedDate] = useState(new Date());

  return (
    <Host matchContents>
      <DatePicker
        title="Select a time"
        selection={selectedDate}
        displayedComponents={['hourAndMinute']}
        onDateChange={date => {
          setSelectedDate(date);
        }}
      />
    </Host>
  );
}
```

## Date and time picker

```tsx
import { useState } from 'react';
import { Host, DatePicker } from '@expo/ui/swift-ui';

export default function DateTimePickerExample() {
  const [selectedDate, setSelectedDate] = useState(new Date());

  return (
    <Host matchContents>
      <DatePicker
        title="Select date and time"
        selection={selectedDate}
        displayedComponents={['date', 'hourAndMinute']}
        onDateChange={date => {
          setSelectedDate(date);
        }}
      />
    </Host>
  );
}
```

## With date range

```tsx
import { useState } from 'react';
import { Host, DatePicker } from '@expo/ui/swift-ui';

export default function DateRangePickerExample() {
  const [selectedDate, setSelectedDate] = useState(new Date());

  return (
    <Host matchContents>
      <DatePicker
        title="Select a date"
        selection={selectedDate}
        displayedComponents={['date']}
        range={{
          start: new Date(2024, 0, 1),
          end: new Date(2024, 11, 31),
        }}
        onDateChange={date => {
          setSelectedDate(date);
        }}
      />
    </Host>
  );
}
```

## Styling with modifiers

You can use the `datePickerStyle` modifier to change the appearance of the picker. Available styles are: `automatic`, `compact`, `graphical`, and `wheel`.

```tsx
import { useState } from 'react';
import { Host, DatePicker } from '@expo/ui/swift-ui';
import { datePickerStyle } from '@expo/ui/swift-ui/modifiers';

export default function WheelDatePickerExample() {
  const [selectedDate, setSelectedDate] = useState(new Date());

  return (
    <Host matchContents>
      <DatePicker
        modifiers={[datePickerStyle('wheel')]}
        title="Select a date"
        selection={selectedDate}
        displayedComponents={['date']}
        onDateChange={date => {
          setSelectedDate(date);
        }}
      />
    </Host>
  );
}
```

```tsx
import { useState } from 'react';
import { Host, DatePicker } from '@expo/ui/swift-ui';
import { datePickerStyle } from '@expo/ui/swift-ui/modifiers';

export default function GraphicalDatePickerExample() {
  const [selectedDate, setSelectedDate] = useState(new Date());

  return (
    <Host matchContents>
      <DatePicker
        modifiers={[datePickerStyle('graphical')]}
        title="Select a date"
        selection={selectedDate}
        displayedComponents={['date']}
        onDateChange={date => {
          setSelectedDate(date);
        }}
      />
    </Host>
  );
}
```

## Disabled picker

You can make the picker non-interactive using the `disabled` modifier.

```tsx
import { useState } from 'react';
import { Host, DatePicker } from '@expo/ui/swift-ui';
import { disabled } from '@expo/ui/swift-ui/modifiers';

export default function DisabledDatePickerExample() {
  const [selectedDate, setSelectedDate] = useState(new Date());

  return (
    <Host matchContents>
      <DatePicker
        title="Select a date"
        selection={selectedDate}
        displayedComponents={['date']}
        onDateChange={date => {
          setSelectedDate(date);
        }}
        modifiers={[disabled()]}
      />
    </Host>
  );
}
```

## Custom locale

Apply the `environment` modifier with the `locale` key to display the picker in a specific locale.

```tsx
import { useState } from 'react';
import { Host, DatePicker } from '@expo/ui/swift-ui';
import { environment } from '@expo/ui/swift-ui/modifiers';

export default function LocaleDatePickerExample() {
  const [selectedDate, setSelectedDate] = useState(new Date());

  return (
    <Host matchContents>
      <DatePicker
        title="Sélectionner la date"
        selection={selectedDate}
        displayedComponents={['date']}
        onDateChange={date => {
          setSelectedDate(date);
        }}
        modifiers={[environment('locale', 'fr_FR')]}
      />
    </Host>
  );
}
```

## Custom time zone

Apply the `environment` modifier with the `timeZone` key to display the picker in a specific IANA time zone.

```tsx
import { useState } from 'react';
import { Host, DatePicker } from '@expo/ui/swift-ui';
import { environment } from '@expo/ui/swift-ui/modifiers';

export default function TimeZoneDatePickerExample() {
  const [selectedDate, setSelectedDate] = useState(new Date());

  return (
    <Host matchContents>
      <DatePicker
        title="Tokyo time"
        selection={selectedDate}
        displayedComponents={['date', 'hourAndMinute']}
        onDateChange={date => {
          setSelectedDate(date);
        }}
        modifiers={[environment('timeZone', 'Asia/Tokyo')]}
      />
    </Host>
  );
}
```

## API

```tsx
import { DatePicker } from '@expo/ui/swift-ui';
```

## Component

### `DatePicker`

Supported platforms: iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[DatePickerProps](#datepickerprops)\>

Renders a SwiftUI `DatePicker` component.

DatePickerProps

### `children`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children to use as a custom label.

### `displayedComponents`

Supported platforms: iOS.

Optional • Type: [DatePickerComponent[]](#datepickercomponent) • Default: `['date']`

The components to display: 'date' and/or 'hourAndMinute'.

### `onDateChange`

Supported platforms: iOS.

Optional • Type: (date: [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)) => void

Callback when the date selection changes.

### `range`

Supported platforms: iOS.

Optional • Type: [DateRange](#daterange)

The selectable date range.

### `selection`

Supported platforms: iOS.

Optional • Type: [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)

The currently selected date.

### `title`

Supported platforms: iOS.

Optional • Type: `string`

A title/label displayed on the picker.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)

## Types

### `DatePickerComponent`

Supported platforms: iOS.

Literal Type: `string`

Acceptable values are: `'date'` | `'hourAndMinute'`

### `DateRange`

Supported platforms: iOS.

| Property | Type | Description |
| --- | --- | --- |
| end(optional) | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | - |
| start(optional) | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | - |
