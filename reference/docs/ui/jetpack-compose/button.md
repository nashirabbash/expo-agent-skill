---
title: "Button"
description: "Jetpack Compose Button components for displaying native Material3 buttons."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/button.md"
scraped_at: "2026-07-15T09:00:54.506538"
---

---
title: Button
description: Jetpack Compose Button components for displaying native Material3 buttons.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Button

Jetpack Compose Button components for displaying native Material3 buttons.
Android, Included in Expo Go

> For cross-platform usage, see the universal [`Button`](/versions/latest/sdk/ui/universal/button.md) — it renders the appropriate native component per platform.

Expo UI provides five button components that match the official Jetpack Compose [Button API](https://developer.android.com/develop/ui/compose/components/button): `Button` (filled), `FilledTonalButton`, `OutlinedButton`, `ElevatedButton`, and `TextButton`. All variants share the same props and accept composable children for content.

| Type | Appearance | Purpose |
| --- | --- | --- |
| Filled | Solid background with contrasting text. | High-emphasis buttons for primary actions such as "submit" and "save." |
| Filled tonal | Background color varies to match the surface. | Also for primary or significant actions. Filled tonal buttons provide more visual weight and suit functions such as "add to cart" and "Sign in." |
| Elevated | Stands out by having a shadow. | Serves a similar purpose to tonal buttons. Increase elevation to make the button appear even more prominently. |
| Outlined | Features a border with no fill. | Medium-emphasis buttons, containing actions that are important but not primary. They pair well with other buttons to indicate alternative, secondary actions like "Cancel" or "Back." |
| Text | Displays text with no background or border. | Low-emphasis buttons, ideal for less critical actions such as navigational links, or secondary functions like "Learn More" or "View details." |

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

### Basic button

A filled button is the default, high-emphasis button for primary actions.

```tsx
import { Host, Button, Text } from '@expo/ui/jetpack-compose';

export default function BasicButtonExample() {
  return (
    <Host matchContents>
      <Button onClick={() => alert('Pressed!')}>
        <Text>Press me</Text>
      </Button>
    </Host>
  );
}
```

### Button variants

Use different button components to convey varying levels of emphasis.

```tsx
import {
  Host,
  Button,
  FilledTonalButton,
  OutlinedButton,
  ElevatedButton,
  TextButton,
  Column,
  Text,
} from '@expo/ui/jetpack-compose';

export default function ButtonVariantsExample() {
  return (
    <Host matchContents>
      <Column verticalArrangement={{ spacedBy: 8 }}>
        <Button onClick={() => {}}>
          <Text>Filled</Text>
        </Button>
        <FilledTonalButton onClick={() => {}}>
          <Text>Filled Tonal</Text>
        </FilledTonalButton>
        <OutlinedButton onClick={() => {}}>
          <Text>Outlined</Text>
        </OutlinedButton>
        <ElevatedButton onClick={() => {}}>
          <Text>Elevated</Text>
        </ElevatedButton>
        <TextButton onClick={() => {}}>
          <Text>Text</Text>
        </TextButton>
      </Column>
    </Host>
  );
}
```

### Button with icons

Since buttons accept composable children, you can add leading and trailing icons using the `Icon` component. This follows the [Material 3 buttons with icon](https://m3.material.io/components/buttons/guidelines) pattern ([official sample](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material3/material3/samples/src/main/java/androidx/compose/material3/samples/ButtonSamples.kt;l=179?q=ButtonWithIconSample)), use 18dp icon size, 8dp spacing between the icon and label.

```tsx
import {
  Host,
  Button,
  OutlinedButton,
  FilledTonalButton,
  Icon,
  Spacer,
  Text,
} from '@expo/ui/jetpack-compose';
import { width } from '@expo/ui/jetpack-compose/modifiers';

const addIcon = require('./assets/add.png');
const sendIcon = require('./assets/send.png');

export default function ButtonWithIconsExample() {
  return (
    <Host matchContents>
      {/* Leading icon */}
      <Button onClick={() => {}}>
        <Icon source={addIcon} size={18} tint="#FFFFFF" />
        <Spacer modifiers={[width(8)]} />
        <Text>Add Item</Text>
      </Button>

      {/* Trailing icon */}
      <OutlinedButton onClick={() => {}}>
        <Text>Send</Text>
        <Spacer modifiers={[width(8)]} />
        <Icon source={sendIcon} size={18} />
      </OutlinedButton>

      {/* Both leading and trailing icons */}
      <FilledTonalButton onClick={() => {}}>
        <Icon source={addIcon} size={18} />
        <Spacer modifiers={[width(8)]} />
        <Text>Create & Send</Text>
        <Spacer modifiers={[width(8)]} />
        <Icon source={sendIcon} size={18} />
      </FilledTonalButton>
    </Host>
  );
}
```

### Custom colors

Override container and content colors using the `colors` prop.

```tsx
import { Host, Button, Text } from '@expo/ui/jetpack-compose';

export default function CustomColorsExample() {
  return (
    <Host matchContents>
      <Button onClick={() => {}} colors={{ containerColor: '#6200EE', contentColor: '#FFFFFF' }}>
        <Text>Purple Button</Text>
      </Button>
    </Host>
  );
}
```

### Custom shape

```tsx
import { Host, Button, Shape, Text } from '@expo/ui/jetpack-compose';

export default function CustomShapeExample() {
  return (
    <Host matchContents>
      <Button
        onClick={() => {}}
        shape={Shape.RoundedCorner({ cornerRadii: { topStart: 16, bottomEnd: 16 } })}>
        <Text>Custom Shape</Text>
      </Button>
    </Host>
  );
}
```

## API

```tsx
import {
  Button,
  FilledTonalButton,
  OutlinedButton,
  ElevatedButton,
  TextButton,
} from '@expo/ui/jetpack-compose';
```

## Components

### `Button`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ButtonProps](#buttonprops)\>

A filled button component.

ButtonProps

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

Content to display inside the button.

### `colors`

Supported platforms: Android.

Optional • Type: [ButtonColors](/versions/v57.0.0/sdk/ui/jetpack-compose/button.md#buttoncolors)

Colors for button elements.

### `contentPadding`

Supported platforms: Android.

Optional • Type: [ButtonContentPadding](#buttoncontentpadding)

The padding between the button container and its content. Use this to adjust internal spacing, for example when adding a leading icon

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the button is enabled for user interaction.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onClick`

Supported platforms: Android.

Optional • Type: `() => void`

Callback that is called when the button is clicked.

### `shape`

Supported platforms: Android.

Optional • Type: [ShapeJSXElement](/versions/v57.0.0/sdk/ui/jetpack-compose/shape.md#shapejsxelement)

The shape of the button.

### `ElevatedButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ButtonProps](#buttonprops)\>

An elevated button component.

### `FilledTonalButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ButtonProps](#buttonprops)\>

A filled tonal button component.

### `OutlinedButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ButtonProps](#buttonprops)\>

An outlined button component.

### `TextButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ButtonProps](#buttonprops)\>

A text button component.

## Types

### `ButtonColors`

Supported platforms: Android.

Colors for button elements.

| Property | Type | Description |
| --- | --- | --- |
| containerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| contentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |

### `ButtonContentPadding`

Supported platforms: Android.

Content padding for the button's inner content. All values are in density-independent pixels (dp).

| Property | Type | Description |
| --- | --- | --- |
| bottom(optional) | `number` | - |
| end(optional) | `number` | - |
| start(optional) | `number` | - |
| top(optional) | `number` | - |
