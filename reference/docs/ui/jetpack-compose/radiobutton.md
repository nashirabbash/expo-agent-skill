---
title: "RadioButton"
description: "A Jetpack Compose RadioButton component for single-selection controls."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/radiobutton.md"
scraped_at: "2026-07-15T09:00:27.382674"
---

---
title: RadioButton
description: A Jetpack Compose RadioButton component for single-selection controls.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# RadioButton

A Jetpack Compose RadioButton component for single-selection controls.
Android, Included in Expo Go

A radio button component for selecting a single option from a set. Maps to the official Jetpack Compose [RadioButton](https://developer.android.com/develop/ui/compose/components/radio-button) API.

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

### Basic radio button

A standalone radio button with an `onClick` handler.

```tsx
import { useState } from 'react';
import { Host, RadioButton } from '@expo/ui/jetpack-compose';

export default function BasicRadioButton() {
  const [selected, setSelected] = useState(false);

  return (
    <Host matchContents>
      <RadioButton selected={selected} onClick={() => setSelected(!selected)} />
    </Host>
  );
}
```

### Radio group (recommended)

The recommended pattern for a radio group follows the [Compose accessibility guidelines](https://developer.android.com/develop/ui/compose/components/radio-button):

-   Wrap the group in a `Column` with the `selectableGroup()` modifier so screen readers treat the options as a group.
-   Apply the `selectable` modifier with `role: 'radioButton'` on each `Row`, making the entire row (including the label) tappable.
-   Pass no `onClick` to the `RadioButton` itself, the row handles the interaction. This provides a larger touch target.

```tsx
import { useState } from 'react';
import { Host, Column, Row, RadioButton, Text } from '@expo/ui/jetpack-compose';
import {
  selectable,
  selectableGroup,
  fillMaxWidth,
  height,
  padding,
} from '@expo/ui/jetpack-compose/modifiers';

export default function RadioGroup() {
  const [selectedOption, setSelectedOption] = useState('Calls');
  const options = ['Calls', 'Missed', 'Friends'];

  return (
    <Host matchContents>
      <Column modifiers={[selectableGroup()]}>
        {options.map(label => (
          <Row
            key={label}
            verticalAlignment="center"
            modifiers={[
              fillMaxWidth(),
              height(56),
              selectable(label === selectedOption, () => setSelectedOption(label), 'radioButton'),
              padding(16, 0, 16, 0),
            ]}>
            <RadioButton selected={label === selectedOption} />
            <Text modifiers={[padding(16, 0, 0, 0)]}>{label}</Text>
          </Row>
        ))}
      </Column>
    </Host>
  );
}
```

## API

```tsx
import { RadioButton } from '@expo/ui/jetpack-compose';
```

## Component

### `RadioButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[RadioButtonProps](#radiobuttonprops)\>

A Material Design radio button.

RadioButtonProps

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onClick`

Supported platforms: Android.

Optional • Type: `() => void`

Callback that is called when the radio button is clicked.

### `selected`

Supported platforms: Android.

Type: `boolean`

Whether the radio button is selected.
