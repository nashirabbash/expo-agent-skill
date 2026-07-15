---
title: "FloatingActionButton"
description: "Jetpack Compose FloatingActionButton components following Material Design 3."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/floatingactionbutton.md"
scraped_at: "2026-07-15T09:00:36.387769"
---

---
title: FloatingActionButton
description: Jetpack Compose FloatingActionButton components following Material Design 3.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# FloatingActionButton

Jetpack Compose FloatingActionButton components following Material Design 3.
Android, Included in Expo Go

Expo UI provides four FloatingActionButton variants matching the Material Design 3 [`FloatingActionButton`](https://developer.android.com/develop/ui/compose/components/fab) API:

-   `SmallFloatingActionButton` — a compact FAB
-   `FloatingActionButton` — the standard FAB (default size)
-   `LargeFloatingActionButton` — a larger FAB
-   `ExtendedFloatingActionButton` — a FAB with an icon and a text label, supporting animated expand/collapse

Each component uses slot-based children (`.Icon` and, for `ExtendedFloatingActionButton`, `.Text`) to compose content.

> **Note:** If you need multiple action buttons in a floating toolbar, use [`HorizontalFloatingToolbar`](/versions/latest/sdk/ui/jetpack-compose/horizontalfloatingtoolbar.md) instead.

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

### Standard FloatingActionButton

```tsx
import { FloatingActionButton, Host, Icon } from '@expo/ui/jetpack-compose';

export default function StandardFABExample() {
  return (
    <Host matchContents>
      <FloatingActionButton onClick={() => console.log('FAB pressed')}>
        <FloatingActionButton.Icon>
          <Icon source={require('./assets/add.xml')} />
        </FloatingActionButton.Icon>
      </FloatingActionButton>
    </Host>
  );
}
```

### FAB variants

```tsx
import {
  FloatingActionButton,
  Host,
  Icon,
  LargeFloatingActionButton,
  SmallFloatingActionButton,
} from '@expo/ui/jetpack-compose';
import { View } from 'react-native';

export default function FABVariantsExample() {
  return (
    <View style={{ flexDirection: 'row', gap: 16 }}>
      <Host matchContents>
        <SmallFloatingActionButton onClick={() => {}}>
          <SmallFloatingActionButton.Icon>
            <Icon source={require('./assets/add.xml')} />
          </SmallFloatingActionButton.Icon>
        </SmallFloatingActionButton>
      </Host>
      <Host matchContents>
        <FloatingActionButton onClick={() => {}}>
          <FloatingActionButton.Icon>
            <Icon source={require('./assets/add.xml')} />
          </FloatingActionButton.Icon>
        </FloatingActionButton>
      </Host>
      <Host matchContents>
        <LargeFloatingActionButton onClick={() => {}}>
          <LargeFloatingActionButton.Icon>
            <Icon source={require('./assets/add.xml')} />
          </LargeFloatingActionButton.Icon>
        </LargeFloatingActionButton>
      </Host>
    </View>
  );
}
```

### ExtendedFloatingActionButton

```tsx
import { ExtendedFloatingActionButton, Host, Icon, Text } from '@expo/ui/jetpack-compose';
import { useState } from 'react';

export default function ExtendedFABExample() {
  const [expanded, setExpanded] = useState(true);

  return (
    <Host matchContents>
      <ExtendedFloatingActionButton expanded={expanded} onClick={() => setExpanded(v => !v)}>
        <ExtendedFloatingActionButton.Icon>
          <Icon source={require('./assets/edit.xml')} />
        </ExtendedFloatingActionButton.Icon>
        <ExtendedFloatingActionButton.Text>
          <Text>Edit</Text>
        </ExtendedFloatingActionButton.Text>
      </ExtendedFloatingActionButton>
    </Host>
  );
}
```

### Floating over content

Use a Compose `Box` with `align('bottomEnd')` to position the FAB over scrollable content entirely within the Compose layer.

```tsx
import {
  Box,
  FloatingActionButton,
  Host,
  Icon,
  LazyColumn,
  ListItem,
} from '@expo/ui/jetpack-compose';
import { align, fillMaxSize, fillMaxWidth, offset } from '@expo/ui/jetpack-compose/modifiers';

export default function FloatingFABExample() {
  return (
    <Host style={{ flex: 1 }}>
      <Box modifiers={[fillMaxSize()]}>
        <LazyColumn modifiers={[fillMaxSize()]}>{/* ...list items... */}</LazyColumn>

        <FloatingActionButton
          modifiers={[align('bottomEnd'), offset(-16, -16)]}
          onClick={() => console.log('pressed')}>
          <FloatingActionButton.Icon>
            <Icon source={require('./assets/add.xml')} />
          </FloatingActionButton.Icon>
        </FloatingActionButton>
      </Box>
    </Host>
  );
}
```

### Custom color

```tsx
import { ExtendedFloatingActionButton, Host, Icon, Text } from '@expo/ui/jetpack-compose';

export default function FABCustomColorExample() {
  return (
    <Host matchContents>
      <ExtendedFloatingActionButton containerColor="#E8DEF8" onClick={() => console.log('pressed')}>
        <ExtendedFloatingActionButton.Icon>
          <Icon source={require('./assets/add.xml')} />
        </ExtendedFloatingActionButton.Icon>
        <ExtendedFloatingActionButton.Text>
          <Text>New item</Text>
        </ExtendedFloatingActionButton.Text>
      </ExtendedFloatingActionButton>
    </Host>
  );
}
```

## API

```tsx
import {
  SmallFloatingActionButton,
  FloatingActionButton,
  LargeFloatingActionButton,
  ExtendedFloatingActionButton,
} from '@expo/ui/jetpack-compose';
```

## Components

### `ExtendedFloatingActionButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ExtendedFloatingActionButtonProps](#extendedfloatingactionbuttonprops)\>

Renders a Material Design 3 `ExtendedFloatingActionButton` with animated label expansion.

Wraps [`ExtendedFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ExtendedFloatingActionButton\(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1\)).

Example

```tsx
import { ExtendedFloatingActionButton, Host, Icon, Text } from '@expo/ui/jetpack-compose';

<Host matchContents>
  <ExtendedFloatingActionButton expanded={true} onClick={() => console.log('pressed')}>
    <ExtendedFloatingActionButton.Icon>
      <Icon source={require('./assets/edit.xml')} />
    </ExtendedFloatingActionButton.Icon>
    <ExtendedFloatingActionButton.Text>
      <Text>Edit</Text>
    </ExtendedFloatingActionButton.Text>
  </ExtendedFloatingActionButton>
</Host>
```

Props for the `ExtendedFloatingActionButton` component.

ExtendedFloatingActionButtonProps

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

Slot-based children (use `.Icon` and `.Text` sub-components).

### `expanded`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Controls whether the label is shown (expanded) or hidden (collapsed).

#### Inherited Props

-   [FloatingActionButtonProps](#floatingactionbuttonprops)

### `FloatingActionButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[FloatingActionButtonProps](#floatingactionbuttonprops)\>

Renders a Material Design 3 standard `FloatingActionButton`.

Wraps [`FloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#FloatingActionButton\(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0\)).

Example

```tsx
import { FloatingActionButton, Host, Icon } from '@expo/ui/jetpack-compose';

<Host matchContents>
  <FloatingActionButton onClick={() => console.log('pressed')}>
    <FloatingActionButton.Icon>
      <Icon source={require('./assets/add.xml')} />
    </FloatingActionButton.Icon>
  </FloatingActionButton>
</Host>
```

Props shared by all `FloatingActionButton` variants.

FloatingActionButtonProps

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

Slot-based children (use `.Icon` sub-component).

### `containerColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The background color of the button container. Defaults to `FloatingActionButtonDefaults.containerColor` (primary container).

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onClick`

Supported platforms: Android.

Optional • Type: `() => void`

Callback invoked when the button is clicked.

### `LargeFloatingActionButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[LargeFloatingActionButtonProps](#largefloatingactionbuttonprops)\>

Renders a Material Design 3 large `FloatingActionButton`.

Wraps [`LargeFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LargeFloatingActionButton\(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0\)).

Example

```tsx
import { LargeFloatingActionButton, Host, Icon } from '@expo/ui/jetpack-compose';

<Host matchContents>
  <LargeFloatingActionButton onClick={() => console.log('pressed')}>
    <LargeFloatingActionButton.Icon>
      <Icon source={require('./assets/add.xml')} />
    </LargeFloatingActionButton.Icon>
  </LargeFloatingActionButton>
</Host>
```

Props for the `LargeFloatingActionButton` component. Same as [`FloatingActionButtonProps`](#floatingactionbuttonprops).

LargeFloatingActionButtonProps

#### Inherited Props

-   [FloatingActionButtonProps](#floatingactionbuttonprops)

### `SmallFloatingActionButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SmallFloatingActionButtonProps](#smallfloatingactionbuttonprops)\>

Renders a Material Design 3 small `FloatingActionButton`.

Wraps [`SmallFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SmallFloatingActionButton\(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0\)).

Example

```tsx
import { SmallFloatingActionButton, Host, Icon } from '@expo/ui/jetpack-compose';

<Host matchContents>
  <SmallFloatingActionButton onClick={() => console.log('pressed')}>
    <SmallFloatingActionButton.Icon>
      <Icon source={require('./assets/add.xml')} />
    </SmallFloatingActionButton.Icon>
  </SmallFloatingActionButton>
</Host>
```

Props for the `SmallFloatingActionButton` component. Same as [`FloatingActionButtonProps`](#floatingactionbuttonprops).

SmallFloatingActionButtonProps

#### Inherited Props

-   [FloatingActionButtonProps](#floatingactionbuttonprops)
