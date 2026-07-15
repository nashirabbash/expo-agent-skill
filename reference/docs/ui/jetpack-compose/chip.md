---
title: "Chip"
description: "Jetpack Compose Chip components for displaying compact elements."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/chip.md"
scraped_at: "2026-07-15T09:00:21.461880"
---

---
title: Chip
description: Jetpack Compose Chip components for displaying compact elements.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Chip

Jetpack Compose Chip components for displaying compact elements.
Android, Included in Expo Go

Expo UI Chips match the official Jetpack Compose [Chip API](https://developer.android.com/develop/ui/compose/components/chip). Each chip type is a separate component: `AssistChip`, `FilterChip`, `InputChip`, and `SuggestionChip`.

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

### Assist chip

Assist chips help users take actions or start tasks, such as booking a flight or opening a map. They often appear as temporary UI elements in response to user input.

```tsx
import { Host, AssistChip, Icon, Text } from '@expo/ui/jetpack-compose';

export default function AssistChipExample() {
  return (
    <Host matchContents>
      <AssistChip onClick={() => console.log('Opening flight booking...')}>
        <AssistChip.Label>
          <Text>Book Flight</Text>
        </AssistChip.Label>
        <AssistChip.LeadingIcon>
          <Icon source={require('./assets/flight.xml')} size={18} />
        </AssistChip.LeadingIcon>
      </AssistChip>
    </Host>
  );
}
```

### Filter chip

Filter chips allow users to refine content from a set of options. They support a selected state and are commonly used in search bars or content filtering.

```tsx
import { useState } from 'react';
import { Host, FilterChip, Text } from '@expo/ui/jetpack-compose';

export default function FilterChipExample() {
  const [selected, setSelected] = useState(false);

  return (
    <Host matchContents>
      <FilterChip selected={selected} onClick={() => setSelected(!selected)}>
        <FilterChip.Label>
          <Text>Images</Text>
        </FilterChip.Label>
      </FilterChip>
    </Host>
  );
}
```

### Input chip

Input chips represent discrete pieces of information entered by a user, such as tags in a text field. They support avatars, trailing icons, and can be dismissed.

```tsx
import { useState } from 'react';
import { Host, InputChip, Icon, Text, FlowRow } from '@expo/ui/jetpack-compose';

export default function InputChipExample() {
  const [chips, setChips] = useState(['Work', 'Travel', 'News']);

  return (
    <Host matchContents>
      <FlowRow horizontalArrangement={{ spacedBy: 8 }}>
        {chips.map(label => (
          <InputChip
            key={label}
            selected
            onClick={() => setChips(prev => prev.filter(c => c !== label))}>
            <InputChip.Label>
              <Text>{label}</Text>
            </InputChip.Label>
            <InputChip.TrailingIcon>
              <Icon source={require('./assets/close.xml')} size={18} />
            </InputChip.TrailingIcon>
          </InputChip>
        ))}
      </FlowRow>
    </Host>
  );
}
```

### Suggestion chip

Suggestion chips help narrow a user's intent by presenting dynamically generated suggestions, such as quick-reply options in a chat or search refinements.

```tsx
import { Host, SuggestionChip, Text } from '@expo/ui/jetpack-compose';

export default function SuggestionChipExample() {
  return (
    <Host matchContents>
      <SuggestionChip onClick={() => console.log('Searching nearby...')}>
        <SuggestionChip.Label>
          <Text>Nearby</Text>
        </SuggestionChip.Label>
      </SuggestionChip>
    </Host>
  );
}
```

## API

```tsx
import { AssistChip, FilterChip, InputChip, SuggestionChip } from '@expo/ui/jetpack-compose';
```

## Components

### `AssistChip`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[AssistChipProps](#assistchipprops)\>

An assist chip that helps users complete actions and primary tasks.

AssistChipProps

### `border`

Supported platforms: Android.

Optional • Type: [ChipBorder](#chipborder)

Border configuration.

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children containing Label, LeadingIcon, and TrailingIcon slots.

### `colors`

Supported platforms: Android.

Optional • Type: [AssistChipColors](#assistchipcolors)

Colors for the chip's container, label, and icons.

### `elevation`

Supported platforms: Android.

Optional • Type: `number`

Elevation in dp.

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the chip is enabled and can be clicked.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onClick`

Supported platforms: Android.

Optional • Type: `() => void`

Callback fired when the chip is clicked.

### `FilterChip`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[FilterChipProps](#filterchipprops)\>

A filter chip component for refining content with selection/deselection.

FilterChipProps

### `border`

Supported platforms: Android.

Optional • Type: [ChipBorder](#chipborder)

Border configuration.

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children containing Label, LeadingIcon, and TrailingIcon slots.

### `colors`

Supported platforms: Android.

Optional • Type: [FilterChipColors](#filterchipcolors)

Colors for the chip's container, label, icon, and selected states.

### `elevation`

Supported platforms: Android.

Optional • Type: `number`

Elevation in dp.

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean`

Whether the chip is enabled and can be interacted with.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onClick`

Supported platforms: Android.

Optional • Type: `() => void`

Callback fired when the chip is clicked.

### `selected`

Supported platforms: Android.

Type: `boolean`

Whether the chip is currently selected.

### `InputChip`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[InputChipProps](#inputchipprops)\>

An input chip that represents user input and can be dismissed.

InputChipProps

### `border`

Supported platforms: Android.

Optional • Type: [ChipBorder](#chipborder)

Border configuration.

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children containing Label, Avatar, and TrailingIcon slots.

### `colors`

Supported platforms: Android.

Optional • Type: [InputChipColors](#inputchipcolors)

Colors for the chip's container, label, icons, and selected states.

### `elevation`

Supported platforms: Android.

Optional • Type: `number`

Elevation in dp.

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the chip is enabled and can be interacted with.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onClick`

Supported platforms: Android.

Optional • Type: `() => void`

Callback fired when the chip is clicked.

### `selected`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `false`

Whether the chip is selected.

### `SuggestionChip`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SuggestionChipProps](#suggestionchipprops)\>

A suggestion chip that offers contextual suggestions and recommendations.

SuggestionChipProps

### `border`

Supported platforms: Android.

Optional • Type: [ChipBorder](#chipborder)

Border configuration.

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children containing Label and Icon slots.

### `colors`

Supported platforms: Android.

Optional • Type: [SuggestionChipColors](#suggestionchipcolors)

Colors for the chip's container, label, and icon.

### `elevation`

Supported platforms: Android.

Optional • Type: `number`

Elevation in dp.

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the chip is enabled and can be clicked.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onClick`

Supported platforms: Android.

Optional • Type: `() => void`

Callback fired when the chip is clicked.

## Types

### `AssistChipColors`

Supported platforms: Android.

Colors for AssistChip.

| Property | Type | Description |
| --- | --- | --- |
| containerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| labelColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| leadingIconContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| trailingIconContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |

### `ChipBorder`

Supported platforms: Android.

Border configuration for chips.

| Property | Type | Description |
| --- | --- | --- |
| color(optional) | [ColorValue](https://reactnative.dev/docs/colors) | Border color. |
| width(optional) | `number` | Border width in dp. Default: `1` |

### `FilterChipColors`

Supported platforms: Android.

Colors for FilterChip.

| Property | Type | Description |
| --- | --- | --- |
| containerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| iconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| labelColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| selectedContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| selectedLabelColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| selectedLeadingIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| selectedTrailingIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |

### `InputChipColors`

Supported platforms: Android.

Colors for InputChip.

| Property | Type | Description |
| --- | --- | --- |
| containerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| labelColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| leadingIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| selectedContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| selectedLabelColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| selectedLeadingIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| selectedTrailingIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| trailingIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |

### `SuggestionChipColors`

Supported platforms: Android.

Colors for SuggestionChip.

| Property | Type | Description |
| --- | --- | --- |
| containerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| iconContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| labelColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
