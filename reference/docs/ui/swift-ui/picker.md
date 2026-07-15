---
title: "Picker"
description: "A SwiftUI Picker component for selecting options from a list."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/picker.md"
scraped_at: "2026-07-15T08:59:28.379496"
---

---
title: Picker
description: A SwiftUI Picker component for selecting options from a list.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Picker

A SwiftUI Picker component for selecting options from a list.
iOS, tvOS, Included in Expo Go

> For cross-platform usage, see the universal [`Picker`](/versions/latest/sdk/ui/universal/picker.md) — it renders the appropriate native component per platform.

Expo UI Picker matches the official SwiftUI [Picker API](https://developer.apple.com/documentation/swiftui/picker) and supports all picker styles via the [`pickerStyle`](/versions/latest/sdk/ui/swift-ui/modifiers.md#pickerstylestyle) modifier.

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

## Segmented picker

```tsx
import { useState } from 'react';
import { Host, Picker, Text } from '@expo/ui/swift-ui';
import { pickerStyle, tag } from '@expo/ui/swift-ui/modifiers';

const options = ['Apple', 'Banana', 'Orange'];

export default function SegmentedPickerExample() {
  const [selectedTag, setSelectedTag] = useState(options[0]);

  return (
    <Host matchContents>
      <Picker
        modifiers={[pickerStyle('segmented')]}
        label="Select a fruit"
        selection={selectedTag}
        onSelectionChange={selection => {
          setSelectedTag(selection);
        }}>
        {options.map(option => (
          <Text key={option} modifiers={[tag(option)]}>
            {option}
          </Text>
        ))}
      </Picker>
    </Host>
  );
}
```

## Menu picker

```tsx
import { useState } from 'react';
import { Host, Picker, Text } from '@expo/ui/swift-ui';
import { pickerStyle, tag } from '@expo/ui/swift-ui/modifiers';

const options = ['Apple', 'Banana', 'Orange'];

export default function MenuPickerExample() {
  const [selectedTag, setSelectedTag] = useState(options[0]);

  return (
    <Host matchContents>
      <Picker
        modifiers={[pickerStyle('menu')]}
        label="Select a fruit"
        selection={selectedTag}
        onSelectionChange={selection => {
          setSelectedTag(selection);
        }}>
        {options.map(option => (
          <Text key={option} modifiers={[tag(option)]}>
            {option}
          </Text>
        ))}
      </Picker>
    </Host>
  );
}
```

## Wheel picker

> The wheel variant is not available on Apple TV.

```tsx
import { useState } from 'react';
import { Host, Picker, Text } from '@expo/ui/swift-ui';
import { pickerStyle, tag } from '@expo/ui/swift-ui/modifiers';

const options = ['Apple', 'Banana', 'Orange'];

export default function WheelPickerExample() {
  const [selectedTag, setSelectedTag] = useState(options[0]);

  return (
    <Host matchContents>
      <Picker
        modifiers={[pickerStyle('wheel')]}
        label="Select a fruit"
        selection={selectedTag}
        onSelectionChange={selection => {
          setSelectedTag(selection);
        }}>
        {options.map(option => (
          <Text key={option} modifiers={[tag(option)]}>
            {option}
          </Text>
        ))}
      </Picker>
    </Host>
  );
}
```

## API

```tsx
import { Picker } from '@expo/ui/swift-ui';
```

## Component

### `Picker`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[PickerProps](#pickerprops)<T\>\>

Displays a native picker component

Example

```tsx
<Picker modifiers={[pickerStyle('segmented')]}>
  <Text modifiers={[tag('option1')]}>Option 1</Text>
  <Text modifiers={[tag(0)]}>Option 3</Text>
</Picker>
```

PickerProps

### `children`

Supported platforms: iOS, tvOS.

Optional • Type: `React.ReactNode`

The content of the picker. You can use `Text` components with `tag` modifiers to display the options.

### `label`

Supported platforms: iOS, tvOS.

Optional • Literal type: `union`

A label displayed on the picker.

Acceptable values are: `string` | `React.ReactNode`

### `onSelectionChange`

Supported platforms: iOS, tvOS.

Optional • Type: `(selection: T) => void`

Callback function that is called when an option is selected. Gets called with the selected `tag` value.

### `selection`

Supported platforms: iOS, tvOS.

Optional • Type: `T`

The selected option's `tag` modifier value.

### `systemImage`

Supported platforms: iOS, tvOS.

Optional • Type: [SFSymbol](https://github.com/nandorojo/sf-symbols-typescript)

The name of the system image (SF Symbol). For example: 'photo', 'heart.fill', 'star.circle'

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
